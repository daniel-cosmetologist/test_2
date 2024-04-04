##########################################

# D. Асинхронные запросы с замером времени

##########################################

import asyncio
import aiohttp
import time

async def measure_requests(url, n=100):
    async with aiohttp.ClientSession() as session:
        start = time.time()
        tasks = [session.get(url) for _ in range(n)]
        await asyncio.gather(*tasks)
        print("Время выполнения:", time.time() - start)

def run():    
    asyncio.run(measure_requests("http://httpbin.org/delay/3"))

