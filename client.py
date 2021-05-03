import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
SERVER_2 = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER_2, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("whats up?!")
send("its late or is it early?")
send(DISCONNECT_MSG)
