import asyncio

from sales_box import SalesBox

sales_box = SalesBox()


async def calculate_stat(app):
    ''' Calculates statistics every second in the last minute
    for average amount per_order and total_sales_amount  '''
    requests_per_min, sales_per_min = [], []
    while True:
        await asyncio.sleep(1)
        if len(requests_per_min) == 60:
            requests_per_min = requests_per_min[1:]
            sales_per_min = sales_per_min[1:]
        requests_per_min.append(sales_box.last_second_requests)
        sales_per_min.append(sales_box.last_second_sales)
        sales_box.last_second_requests = 0
        sales_box.last_second_sales = 0
        try:
            sales_box.average_amount_per_order = round(
                sum(sales_per_min)/sum(requests_per_min), 2
            )
            sales_box.total_sales_amount = sum(sales_per_min)
        except ZeroDivisionError:
            sales_box.average_amount_per_order = 0
            sales_box.total_sales_amount = 0
            continue


async def start_calculate_stat(app):
    app['calculate_stat_listener'] = asyncio.create_task(calculate_stat(app))
