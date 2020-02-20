import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    print(f"Connected: {addr[0]}:{addr[1]}")
    data = conn.recv(10240)
    print(data.decode('utf-8'))
conn.close()
