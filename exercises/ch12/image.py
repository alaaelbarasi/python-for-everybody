import socket

mysocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('www.data.pr4e.org',80))
mysocket.sendall(b'GET http://www.data.pr4e.org/cover3.jpg HTTP/1.0 \r\n\r\n')
count=0
picture=b''
while True:
    data=mysocket.recv(5120)
    if len(data)<1: break
    count=count+len(data)
    print(len(data), count)
    picture=picture+data
mysocket.close()


print('All good')