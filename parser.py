def parser(msg):
    msgType, msgBody = msg.split(":")
    if not msgType in ['msg', 'room', 'username', 'info']:
        raise SyntaxError("unknow type in msg:\n{}".format(msg))
    if not msgType or not msgBody:
        raise SyntaxError("syntax error in msg: \n{}".format(msg))
    return msgType, msgBody