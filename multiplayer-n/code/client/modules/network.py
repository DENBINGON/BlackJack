import socket
def init():
    sock = socket.socket()
    sock.connect(('localhost', 9090))
def send(data):
    try:
        sock.send((data).encode('utf-8'))
    except:
        sock.send(('Error connection').encode('utf-8'))
def close():
    sock.close()
