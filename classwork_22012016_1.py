from socket import socket
from time import  sleep
from threading import Thread
from datetime import datetime
from web_library import users
import importlib
from urllib.parse import parse_qs

time = datetime.now()
s = socket()
s.bind(('localhost', 2222))
s.listen(0)

def handle_request(conn):
    with conn:
        request = conn.recv(1024)
        path = request.decode('utf8').split()[1]

        if path == '/':
            body = """
            <html><head><title>server</title></head><body>
                <form action = "/login">
                    <input name = "username"></br>
                    <input name = "password"></br>
                    <input type = "submit"></br>
                </form>
            </body></html>
            """

            conn.sendall(('HTTP/1.1 200 ok \r\n\r\n' + body).encode('utf8'))
        elif path.startswith('/login'):
            print('login', request)

            print(users())
            str_qs = path[7:]
            print(str(parse_qs(str_qs)))
            print(str_qs)
            conn.sendall(('HTTP/1.1 200 Ok \r\n\r\nWelcome').encode('utf8'))
        else:
            conn.sendall(('HTTP/1.1 404 Nope \r\n\r\n').encode('utf8'))


while True:
    conn, addr = s.accept()
    handle_request(conn)