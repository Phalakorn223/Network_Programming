import socket

UDP_IP = "10.4.60.138"
UDP_PORT = 5005
MESSAGE = b"Hello, Test"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))