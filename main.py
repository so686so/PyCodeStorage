# IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
import os


# IMPORT CORE
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
from Core.CodeManage    import CodeManage
from CoreDefine         import *


PATH = r''

CodeListDict = {}


# json = JsonManage()
# json.openJsonFile(JSON_PATH)
# CodeListDict = json.getJsonDict()

# ChoiceProgram = 'AttributeProgram'

# PATH = CodeListDict[ChoiceProgram]['Path']
# FILE = CodeListDict[ChoiceProgram]['RunFileName']

# print(f'START : {PATH} -> {FILE}')
# os.chdir(PATH)
# a = subprocess.run(f'python {FILE}')

if __name__ == "__main__":
    CM = CodeManage()
    
    Num = CM.getNumByAlias('AttributeProgram')
    print(f'> SelectNum : {Num}')
    
    CM.moveTargetDir(CM.getCodePathList()[Num])
    CM.runCode(CM.getCodeFileNameList()[Num])
