import poplib
from email.message import EmailMessage

server = "192.168.146.132"
user = "phalakorn"
passwd = "phalakornpk223"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum) :
    for msg in server.retr(i + 1)[1] :
        print(msg.decode())