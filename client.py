import select
import json
import socket
import sys
if __name__ == '__main__':
    setting_json = open('setting.json', 'r').read()
    data_json = json.loads(setting_json)
    user_name = data_json['client']['username']
    server_ip = data_json['server']['ip']
    server_port = int(data_json['server']['port'])
    if user_name == '':
        user_name = input('enter user name:\n')
    if server_ip == '':
        server_ip = int(input('enter server ip:\n'))
    print('starting ')
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.connect((server_ip, server_port ))
    while True:
        readList, _, _ = select.select([sys.stdin, tcpsock], [], [], 2)
        if (readList):
            for obj in readList:
                if (obj == sys.stdin):
                    readMsg = input()
                    print("get msg{}".format(readMsg))
                    tcpsock.send(readMsg.encode('utf-8')) #TODO
                else:
                    recvMsg = tcpsock.recv(1024)
                    print(recvMsg)
                    print("recv")
        else:
            print ("2s passed")