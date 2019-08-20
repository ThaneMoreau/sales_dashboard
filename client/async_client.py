import asyncio
import random
import time

import aiohttp


async def push(session, url, headers, params):
    '''Posts request to sales endpoint'''
    await session.post(url, headers=headers, params=params)


async def run(requests_amount, sales_amount):
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    params = {'sales_amount': sales_amount}
    async with aiohttp.ClientSession() as session:
        for i in range(requests_amount):
            await push(
                session,
                'http://localhost:8080/sales',
                headers=headers,
                params=params
            )


if __name__ == "__main__":
    start = time.monotonic()
    asyncio.run(
        run(
            requests_amount=10000,
            sales_amount=random.randint(0, 10**6)
        )
    )
    print(f'TOTLA TIME: {time.monotonic() - start}')
