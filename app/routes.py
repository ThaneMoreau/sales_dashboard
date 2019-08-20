from views import Transactions, Statistics


def setup_routes(app, app_root):
    app.router.add_view('/statistics', Statistics)
    app.router.add_view('/sales', Transactions)
    app.router.add_static('/static/', app_root / 'static', name='static')
    app['static_root_url'] = '/static'
