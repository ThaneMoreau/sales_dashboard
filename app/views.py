from sales_stat import sales_box
import aiohttp_jinja2
import jinja2
from aiohttp import web
import json


class Statistics(web.View):

    @aiohttp_jinja2.template('statistics.html')
    async def get(self):
        context = {
                'total_sales_amount': sales_box.total_sales_amount,
                'average_amount_per_order': sales_box.average_amount_per_order,

        }
        if self.request.headers.get('X-Requested-With'):
            return web.json_response(json.dumps(context))
        return context


class Transactions(web.View):

    async def post(self):
        try:
            sales_per_request = float(
                self.request.rel_url.query['sales_amount']
            )
            assert int(sales_per_request) == sales_per_request
            assert sales_per_request > 0
        except (KeyError, AssertionError):
            return web.Response(status=422)
        sales_box.last_second_requests += 1
        sales_box.last_second_sales += float(sales_per_request)
        # sales_box.total_sales_amount += float(sales_per_request)
        return web.Response(status=202)
