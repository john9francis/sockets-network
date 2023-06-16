# echo-server.py
# from realpython.com

import socket

HOST = "0.0.0.0"  # Trying to bind to all network interfaces
PORT = 60000  # Port to listen on (non-privileged ports are > 1023)

# three requests that the server can respond to
request1 = "Echo"
request2 = "Tell a joke"
request3 = "Access a database"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            print(f"Would you like me to 1.{request1}, 2.{request2}, or 3.{request3}?")
            print('(Please enter "1", "2", or "3".)')
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(f'You chose: {data}.')
