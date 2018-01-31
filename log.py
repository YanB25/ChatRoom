import json
VERBOSE = 0
WARNING = 1
ERROR = 2

def log(msg, level):
    '''
    used to print log imformation
    '''
    if level == -1:
        setting_json = open('setting.json', 'r').read()
        json_data = json.loads(setting_json)
        log_level_msg = json_data['server']['logLevel']
        if log_level_msg == "VERBOSE":
            log.level = VERBOSE
        elif log_level_msg == "WARNING":
            log.level = WARNING
        else:
            log.level = ERROR
    if level >= log.level:
        print(msg)
log.level = -1
