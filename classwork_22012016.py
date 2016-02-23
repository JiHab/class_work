from socket import socket
from time import  sleep
from threading import Thread
from datetime import datetime
import importlib
time = datetime.now()
s = socket()
s.bind(('localhost', 2222))
s.listen(0)

def handle_request(conn):
    with conn:
        ul = ''
        str_now = str(datetime.now())
        print('request:', conn.recv(1024))
        request = conn.recv(1024)
        try:
            path = request.decode('utf8').split()[1]
            module_name = path[1:]
            module = importlib.import_module(module_name)
            functions = dir(module)
            ul = '<ul>'
            for f in functions:
                ul += '<li>%s</li>' % f
                ul += '</ul>'
        except:
            print('ololo')
        str_dir = str(dir(datetime))
        mess = """HTTP/1.1 200 ok

                <html><head><title>server</title></head><body> hello, ama server """ + str_now + '<li></li>' + str_dir + ul + """</body>"""
        conn.sendall(mess.encode('utf8'))


while True:
    conn, addr = s.accept()
    handle_request(conn)