import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.send(b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512).decode() # must use decode() for python3 or we'll get bytes back instead
    if ( len(data) < 1 ) :
        break
    print(data);

mysock.close()
