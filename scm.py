import re
from adb import *
from consts import *

def execute_register_scm(svc_id, cmd_id, args):
        '''
        Sends a register SCM using fuzz_zone with the given arguments.
        Returns the error value returned by the IOCTL
        '''
        if len(args) > REGISTER_SCM_SUPPORTED_ARGS:
                raise "Execute register SCM currently supports only up to %d parameters" % REGISTER_SCM_SUPPORTED_ARGS
        args_str = " ".join(["%08X" % arg for arg in args]).strip()
        command_str = "%s reg %d %d %d %s" % (FUZZ_ZONE_PATH, svc_id, cmd_id, len(args), args_str)
        resp_str = execute_privileged_command(command_str)
        if resp_str.find("Failed") >= 0:
                raise "Failed to send register SCM! %s" % resp_str
        return int(re.search("^IOCTL RES: (\d+)", resp_str, re.MULTILINE).group(1))

def execute_raw_scm(svc_id, cmd_id, request_data, response_length):
        '''
        Sends a "normal" SCM using fuzz_zone with the given arguments, and returns the resulting buffer
        '''
        
        resp = execute_privileged_command("%s raw %d %d %s %d" % (FUZZ_ZONE_PATH, svc_id, cmd_id, request_data.encode("hex"), response_length))
        return resp.split("\n")[-2].decode("hex")

