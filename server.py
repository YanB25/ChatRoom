import sys
import select
import socket
import log

class ChatRoom(object):
    '''
    main class for server
    usage:
    chatRoom = ChatRoom()
    chatRoom.run(<port>)
    '''
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', self.port))
        self.socket.listen(10)
        self.descriptors = [self.socket]
        log.log("init socket in port " + str(port), log.VERBOSE)
    
    def run(self):
        log.log("start running ...", log.VERBOSE)
        while True:
            readList, _, _ = select.select(self.descriptors, [], [], 2)
            if readList:
                for sock in readList:
                    if sock == self.socket:
                        # new connection is joining
                        self.add_new_connection()
                    else:
                        msg = sock.recv(1024)
                        host, port = sock.getpeername()
                        if (msg):
                            # broadcast
                            self.broadcase_message(msg)
                        else:
                            # disconnect
                            bs = "{}:{} disconnect".format(str(host), str(port))
                            self.broadcase_message(bs)
                            sock.close()
                            self.descriptors.remove(sock)
    
    def add_new_connection(self):
        connectionSocket, addr = self.socket.accept()
        self.descriptors.append(connectionSocket)
        bs = "{} join the chat room".format(str(addr))
        self.broadcase_message(bs)
        
    def broadcase_message(self, msg):
        log.log("broadcasting {}".format(msg), log.VERBOSE)
        for sock in self.descriptors:
            if (sock != self.socket):
                if (type(msg) is str): msg = msg.encode('utf-8')
                sock.send(msg)

if __name__ == "__main__":
    chatRoom = ChatRoom(12000)
    chatRoom.run()






