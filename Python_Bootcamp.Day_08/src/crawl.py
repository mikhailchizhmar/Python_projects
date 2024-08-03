import aiohttp
import asyncio
import sys


async def submit_urls(urls):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8888/api/v1/tasks/", json={"urls": urls}) as response:
            task = await response.json()
            return task["id"]


async def check_task_status(task_id):
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(f"http://localhost:8888/api/v1/tasks/{task_id}") as response:
                task = await response.json()
                if task["status"] == "ready":
                    return task["result"], task["urls"]
            await asyncio.sleep(1)


async def main(urls):
    task_id = await submit_urls(urls)
    result, urls = await check_task_status(task_id)
    for code, url in zip(result, urls):
        print(f"{code}\t{url}")


if __name__ == "__main__":
    urls = sys.argv[1:]
    asyncio.run(main(urls))
