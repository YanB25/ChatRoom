import select
import json
import socket
import sys
import parser
def beforeStart():
    '''
    read setting.json, check all the necessary data
    if not provided, ask the user to input
    '''
if __name__ == '__main__':
    readFile = open('setting.json', 'r')
    setting_json = readFile.read()
    data_json = json.loads(setting_json)
    user_name = data_json['client']['username']
    server_ip = data_json['server']['ip']
    server_port = int(data_json['server']['port'])
    if user_name == '':
        user_name = input('enter user name:\n')
    if server_ip == '':
        server_ip = input('enter server ip:\n')
    data_json['client']['username'] = user_name
    data_json['server']['ip'] = server_ip
    readFile.close()
    new_json = json.dumps(data_json)
    writeFile = open('setting.json', 'w')
    writeFile.write(new_json)
    writeFile.close()

    roomNumber = input('enter room number:')
    print('starting ')
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.connect((server_ip, server_port ))

    tcpsock.send("room:{}".format(roomNumber))
    tcpsock.send("username:{}".format(user_name))
    while True:
        readList, _, _ = select.select([sys.stdin, tcpsock], [], [], 2)
        if (readList):
            for obj in readList:
                if (obj == sys.stdin):
                    readMsg = input()
                    #print("get msg{}".format(readMsg))
                    tcpsock.send("msg:{}".format(readMsg).encode('utf-8'))
                else:
                    recvMsg = tcpsock.recv(1024)
                    recvMsg = recvMsg.decode()
                    try:
                        t, b = parser.parser(recvMsg)
                        if (t == 'msg'):
                            print(recvMsg)
                    except:
                        print("unknown msg recieve from server")
        else:
            #print ("2s passed")
            pass