from urllib.parse import parse_qs
from wsgiref.simple_server import make_server


def calc(env, start_response):
  if '/' == env['PATH_INFO']:
    start_response('200 OK', [])
    return [b'<html><form action="/eval"><input name="expression"><input type="submit"></form></body>']
  elif '/eval' == env['PATH_INFO']:
    query = parse_qs(env['QUERY_STRING'])
    print(query)
    expression = query['expression'][0]
    result = eval(expression)
    start_response('200 OK', [])
    return [str(result).encode('utf-8')]


def plusone(env,start_response,fun):
    if '/eval' == env['PATH_INFO']:
        return int(fun())+1

if __name__ == '__main__':
    httpd = make_server('', 8000, plusone(calc))
    httpd.serve_forever()