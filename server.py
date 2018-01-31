import sys
import select
import socket
import log
import parser

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
        self.ipToName = {}
        self.roomToSocks = {}
        self.ipToRoom = {}
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
                        if (msg):
                            host, port = sock.getpeername()
                            msgType, msgBody = parser.parser(msg)
                            if msgType == 'username':
                                self.ipToName[host] = msgBody
                                log.log("ip {} as username {}".format(host, msgBody), log.VERBOSE)
                                room = self.ipToRoom[host]
                                bs = "user {} enter room {}".format(msgBody, room)
                                self.broadcase_message(room, bs)
                            elif msgType == 'room':
                                self.ipToRoom[host] = msgBody
                                r = self.roomToSocks.get(msgBody)
                                if (r == None):
                                    self.roomToSocks[msgBody] = [sock]
                                else:
                                    self.roomToSocks[msgBody].append = sock
                                log.log("enter room{}".format(msgBody),log.VERBOSE)
                            elif msgType == 'msg':
                                # broadcast
                                room = self.ipToRoom[host]
                                self.broadcase_message(room, msg, sock)
                            else:
                                log.log("unknown syntax recieved:{}".format(msg), log.WARNING)
                        else:
                            # disconnect
                            bs = "{}:{} disconnect".format(str(host), str(port))
                            room = self.ipToRoom[host]
                            self.broadcase_message(room, bs)
                            sock.close()
                            self.descriptors.remove(sock)
                            del self.ipToRoom[host]
                            del self.ipToName[host]
                            del self.roomToSocks[room]
    
    def add_new_connection(self):
        connectionSocket, addr = self.socket.accept()
        self.descriptors.append(connectionSocket)
        bs = "{} join the chat room".format(str(addr))
        
    def broadcase_message(self, room, msg, ignore = None):
        log.log("broadcasting {}".format(msg), log.VERBOSE)
        for sock in self.roomToSocks[room]:
            if (sock != self.socket and sock != ignore):
                if (type(msg) is str): msg = msg.encode('utf-8')
                sock.send(msg)

if __name__ == "__main__":
    chatRoom = ChatRoom(12000)
    chatRoom.run()






