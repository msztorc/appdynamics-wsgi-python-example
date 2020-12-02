from appdynamics.agent import api as appd

def application(environ, start_response):
    custom_bt = appd.start_bt('Custom BT example app')
    e = None
    try:
        start_response('200 OK', [('Content-Type', 'text/html')])
    except Exception as e:
        raise
    finally:
        appd.end_bt(custom_bt, e)

    yield 'Hello '.encode('utf-8')
    yield b'World\n'
