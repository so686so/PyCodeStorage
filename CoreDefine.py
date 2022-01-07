# Program Info
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
TITLE   = 'PyCode Storage Program'
DATE    = '2022-01-05'
VERSION = '1.0.0'
IDE     = 'Visual Studio Code 1.62.0'
OS      = 'Windows 10'
AUTHOR  = 'SO BYUNG JUN'


# CONST Defines
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
ERROR_STRICT_HARD = 0
ERROR_STRICT_SOFT = 1


# VAR Defines
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
CORE_SHOW_LOG       = True              # 터미널 창에 로그가 나오게 하는지 총괄하는 시스템 변수
CORE_TEST_MODE      = False
CORE_ERROR_STRICT   = ERROR_STRICT_SOFT # 에러 발생 시, 처리 정도를 결정하는 시스템 변수


# IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
import sys


# OTHER DEFINES
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
CORE_ENCODING_FORMAT    = 'utf-8'                       # 파일 Read 할 때, 인코딩 포맷


# VAR
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
JSON_PATH   = r'./Data/CodeList.json'
EACH_PATH   = 'Path'
EACH_EXE    = 'RunFileName'

# Link VAR
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
CORE_LINK_DICT  = {}
LINK_NAME_LIST  = 0
CORE_SAVE_VALUE = 1

# FunctionDefine
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
def setCoreValue(CoreName, Value):
    globals()[CoreName] = Value

def getCoreValue(CoreName):
    return globals()[CoreName]