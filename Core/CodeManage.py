# IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
import os
import sys
import subprocess


# Add Import Path
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))



# Custom Modules
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from Core.JsonManage             import *
from Core.CommonUse              import *


# Refer to CoreDefine.py
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from CoreDefine             import *


# CONST DEFINE
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
PROGRAM_LIST_ALIAS      = 0
PROGRAM_LIST_CODE_PATH  = 1
PROGRAM_LIST_CODE_NAME  = 2

PROGRAM_DICT_CODE_PATH  = 0
PROGRAM_DICT_CODE_NAME  = 1

# CodeManage Class
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
class CodeManage:
    def __init__(self, jsonPath:str=JSON_PATH) -> None:
        self.JM = JsonManage()
        self.JM.openJsonFile(jsonPath)
        
        assert self.JM.checkValidCreate() is True
        
        self.jsonDict = self.JM.getJsonDict()
        self.selectCodeNum = -1
        
        
    def getCodeTotalList(self) -> list:
        resList = []
        for k, v in self.jsonDict.items():
            resList.append([k, v[EACH_PATH], v[EACH_EXE]])
        return resList
    

    def getCodeAliasesList(self) -> list:
        resList = []
        for eachKey in self.jsonDict.keys():
            resList.append(eachKey)
        return resList
    

    def getCodePathList(self) -> list:
        resList = []
        for eachVal in self.jsonDict.values():
            resList.append(eachVal[EACH_PATH])
        return resList
    
    
    def getCodeFileNameList(self) -> list:
        resList = []
        for eachVal in self.jsonDict.values():
            resList.append(eachVal[EACH_EXE])
        return resList
    
    
    def checkOverwrittenAlreadyUseAlias(self, searchAlias:str) -> bool:
        originAliasList = self.getCodeAliasesList()
        if searchAlias in originAliasList:
            return True
        else:
            return False
        
        
    def moveTargetDir(self, targetDir:str) -> bool:
        if os.path.isdir(targetDir) is False:
            return False
        
        os.chdir(targetDir)
        return True
    
    
    def getNumByAlias(self, targetAlias:str) -> int:
        returnInt = -1
        AliasList = self.getCodeAliasesList()
        for idx, eachAlias in enumerate(AliasList):
            if targetAlias == eachAlias:
                returnInt = idx
        return returnInt
    
    
    def checkRealExistFileByAlias(self, targetAlias:str) -> bool:
        targetNum = self.getNumByAlias(targetAlias)

        if targetNum == -1:
            return False
    
        fullList = self.getCodeTotalList()
        target   = fullList[targetNum]
        fullPath = os.path.join(target[PROGRAM_LIST_CODE_PATH], target[PROGRAM_LIST_CODE_NAME])
        
        if os.path.isfile(fullPath):
            return True
        else:
            return False
    
    
    def runCode(self, targetExe:str) -> bool:
        subprocess.run(f'python {targetExe}')