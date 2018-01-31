# ChatRoom
学习web,socket时的练手小项目。  
并没有特别厉害  
## feature
- chating with your friend through terminal
## usage
### download
``` sh
>>> git clone git@github.com:YanB25/ChatRoom.git
```
### requisite
- python3 version 3.5 or above
- Unix System(maybe)
### usage for server
``` sh
>>> python server.py
init socket int port <port>
start running...
```
the following two lines indicate success  
### usage for client
``` sh
>>> python client.py
enter user name:
... <user name>
enter server ip:
... <server ip> # like 172.0.0.1
starting  
connect successfully  
enter room number: # enter a number like 100
```
When you initially run the app, you are required to enter \<user name\> and \<server ip address\>.  
Your username will be shown in your chatting room.  
You are free to set you configuration on `setting.json`  
## notice
- Run a server before clients' connection
- You can run a server and clients on the same computer. In this case, set the server ip to 127.0.0.1
## application-layer protocol
The app used a simple(or naive) protocal, which relies on TCP protocol.  
The message in the protocol follows such a pattern, a string encoded by `utf-8`
```
<key>:<value>\n
[<key>:<value>\n
[<key>:<value>\n]...]
```
Where key is one of `msg`, `username`and`room`.  
Value is any data.

## Bugs or Advice
Feel free to create an issue.