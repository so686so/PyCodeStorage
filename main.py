# IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
import os


# IMPORT CORE
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
from Core.CodeManage    import CodeManage
from CoreDefine         import *


if __name__ == "__main__":
    CM = CodeManage()
    
    Num = CM.getNumByAlias('AttributeProgram')
    # Num = CM.getNumByAlias('PyToggle')
    
    print(f'> SelectNum : {Num}')
    print(f'> Move Dir  : {CM.getCodePathList()[Num]}')
    print(f'> Run File  : {CM.getCodeFileNameList()[Num]}')
    
    CM.moveTargetDir(CM.getCodePathList()[Num])
    CM.runCode(CM.getCodeFileNameList()[Num])
