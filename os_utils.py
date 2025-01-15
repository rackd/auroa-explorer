import os
import platform

UNIX = 0
WIN = 1
JAVA = 2
NOT_INIT = -1

global _C_OS_TYPE = NOT_INIT

def getOS():
    return _C_OS_TYPE

def init():
    match(os.name):
        case 'posix':
            C_OS_TYPE = UNIX
        case 'nt':
             C_OS_TYPE = WIN
        case 'java':
             C_OS_TYPE = JAVA
