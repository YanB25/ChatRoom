import log
def parser(msgs):
    log.log(msgs, log.VERBOSE)
    if not type(msgs) is str: 
        msgs = msgs.decode()
    msgs = msgs.split("\n")
    rets = []
    for msg in msgs:
        if(not msg):continue
        pos = msg.find(":")
        msgType = msg[0:pos]
        msgBody = msg[pos+1:]
        if not msgType in ['msg', 'room', 'username', 'info']:
            log.log("unknown type:\n{}".format(msg), log.WARNING)
        if not msgType or not msgBody:
            log.log("can not parse:\n{}".format(msg), log.WARNING)
        rets.append((msgType, msgBody))
    return rets