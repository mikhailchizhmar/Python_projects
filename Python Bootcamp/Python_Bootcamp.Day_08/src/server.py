from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import asyncio
import httpx
import uvicorn

app = FastAPI()

tasks = {}


class Task(BaseModel):
    id: str
    status: str
    urls: list[str]
    result: list[int] = None


class TaskRequest(BaseModel):
    urls: list[str]


@app.post("/api/v1/tasks/", status_code=201)
async def create_task(task_request: TaskRequest):
    task_id = str(uuid.uuid4())
    task = Task(id=task_id, status="running", urls=task_request.urls, result=[])
    tasks[task_id] = task
    asyncio.create_task(process_task(task_id))
    return task


async def process_task(task_id: str):
    task = tasks[task_id]
    async with httpx.AsyncClient() as client:
        for url in task.urls:
            try:
                response = await client.get(url)
                task.result.append(response.status_code)
            except httpx.HTTPStatusError as exc:
                task.result.append(exc.response.status_code)
            except Exception:
                task.result.append(0)
    task.status = "ready"


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
