import socket
import threading

ip = "127.0.0.1"  # local server
port = 5000

def attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        s.close()
    except:
        pass

for i in range(200):
    thread = threading.Thread(target=attack)
    thread.start()
