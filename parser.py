import log
def parser(msgs):
    log.log(msgs, log.VERBOSE)
    if not (msgs is str): 
        msgs = msgs.decode()
    msgs = msgs.split("\n")
    rets = []
    for msg in msgs:
        if(not msg):continue
        msgType, msgBody = msg.split(":")
        if not msgType in ['msg', 'room', 'username', 'info']:
            log.log("unknown type:\n{}".format(msg), log.WARNING)
        if not msgType or not msgBody:
            log.log("can not parse:\n{}".format(msg), log.WARNING)
        rets.append((msgType, msgBody))
    return rets