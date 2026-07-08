import socket

try:
    print("Fully qualified domain name:", socket.getfqdn("8.8.8.8"))
    print("Host name:", socket.gethostbyname("www.python.org"))
    print("Host name:" + str(socket.gethostbyname_ex("www.python.org")))
    print("Get host name:" + socket.gethostname())
except Exception as err:
    print("Error:", str(err))