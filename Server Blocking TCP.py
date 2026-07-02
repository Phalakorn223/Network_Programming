import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1234 if len(sys.argv) == 1 else int(sys.argv[1])
sock.bind(('localhost', port))
sock.listen(5)

try: