import wsgiserver
from appdynamics.agent import api as appd

def application(environ, start_response):
    custom_bt = appd.start_bt('Custom BT')
    body_str = 'Hello world!\n'
    body_str_byte = bytes(body_str, 'utf-8')
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    e = None
    try:
        start_response(status, headers)
    except Exception as e:
        raise
    finally:
        appd.end_bt(custom_bt, e)


    return [body_str_byte]


def my_orders(environ, start_response):
    custom_bt = appd.start_bt('My orders BT')
    body_str = 'My orders\n'
    body_str_byte = bytes(body_str, 'utf-8')
    status = '200 OK'
    headers = [('Content-type', 'text/text')]

    e = None
    try:
        start_response(status, headers)
    except Exception as e:
        raise
    finally:
        appd.end_bt(custom_bt, e)

    return [body_str_byte]


d = wsgiserver.WSGIPathInfoDispatcher({'/': application, '/orders': my_orders})

server = wsgiserver.WSGIServer(d)
server.start()