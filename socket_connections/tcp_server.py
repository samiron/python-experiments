import socket
#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
#serversocket.bind((socket.gethostname(), 1298))
serversocket.bind(('localhost', 1298))
#become a server socket
serversocket.listen(5)

while 1:
    #accept connections from outside
    print "Waiting: "
    (clientsocket, address) = serversocket.accept()
    
    while 1:
        print "Receiving data: "
        data = clientsocket.recv(1024)
        if not data: 
            print "No data Found. Exiting current connection."
            break
        else:
            print "Received data: " + data
        
        reply = eval(data)
        clientsocket.sendall(str(reply))
        
    print "Closing connection"
    clientsocket.close()
    
