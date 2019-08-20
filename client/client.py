import random
import time

import requests


def run(requests_amount, sales_amount):
    url = 'http://localhost:8080/sales'
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    params = {'sales_amount': sales_amount}
    for i in range(requests_amount):
        # time.sleep(random.randint(0, 10) * 0.001)
        # time.sleep(1)
        requests.post(
            url=url,
            params=params,
            headers=headers
        )


if __name__ == "__main__":
    start = time.monotonic()
    run(
        requests_amount=10000,
        sales_amount=random.randint(0, 10**6)
    )
    print(f'TOTAL TIME: {time.monotonic() - start}')
