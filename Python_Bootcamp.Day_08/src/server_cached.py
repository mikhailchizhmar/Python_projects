from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import asyncio
import httpx
import redis.asyncio as redis
import uvicorn
from urllib.parse import urlparse

app = FastAPI()


tasks = {}
REDIS_URL = "redis://localhost:6379"
CACHE_EXPIRY = 3600  # 1 hour


class Task(BaseModel):
    id: str
    status: str
    urls: list[str]
    result: list[int] = None


class TaskRequest(BaseModel):
    urls: list[str]


@app.on_event("startup")
async def startup_event():
    app.state.redis = redis.Redis.from_url(REDIS_URL)


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()


@app.post("/api/v1/tasks/", status_code=201)
async def create_task(task_request: TaskRequest):
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, status="running", urls=task_request.urls, result=[])
    tasks[task_id] = task
    asyncio.create_task(process_task(task_id, task_request.urls))
    return task


async def process_task(task_id: str, urls: list[str]):
    task = tasks[task_id]
    redis_client = app.state.redis
    async with httpx.AsyncClient() as client:
        for url in urls:
            domain = urlparse(url).netloc
            await redis_client.incr(f"domain:{domain}")

            cached_status = await redis_client.get(f"url:{url}")
            if cached_status:
                task.result.append(int(cached_status))
            else:
                try:
                    response = await client.get(url)
                    task.result.append(response.status_code)
                    await redis_client.set(f"url:{url}", response.status_code, ex=CACHE_EXPIRY)
                except httpx.HTTPStatusError as exc:
                    task.result.append(exc.response.status_code)
                    await redis_client.set(f"url:{url}", exc.response.status_code, ex=CACHE_EXPIRY)
                except Exception:
                    task.result.append(0)
                    await redis_client.set(f"url:{url}", 0, ex=CACHE_EXPIRY)
    task.status = "ready"


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
