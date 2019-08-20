import asyncio
import pathlib

import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import setup_routes
from sales_stat import calculate_stat, start_calculate_stat

TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'
APP_ROOT = pathlib.Path(__file__).parent.parent

app = web.Application()
setup_routes(app, APP_ROOT)
aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(TEMPLATES_ROOT))
    )

app.on_startup.append(start_calculate_stat)
web.run_app(app)
