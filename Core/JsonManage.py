# IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
import os
import sys
import json


# Add Import Path
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))


# Custom Modules
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from Core.CommonUse         import *


# Refer to CoreDefine.py
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from CoreDefine             import *


# JsonManage Class
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
class JsonManage:
    def __init__(self, initDict:dict={}) -> None:
        self.jsonPath = r''
        self.jsonDict = initDict.copy()


    def checkValidCreate(self) -> bool:
        returnRes = True
        returnRes &= self.checkJsonDictType()
        
        return returnRes


    def openJsonFile(self, filePath:str) -> bool:
        # try 실패 대비해서 백업하고나서 클리어
        tmpBackUpDict = self.jsonDict.copy()
        self.jsonDict.clear()

        try:
            with open(filePath, 'r') as rf:
                self.jsonDict = json.load(rf)
            return True

        except Exception as e:
            ErrorLog(f'[openJsonFile] -> {e}', lineNum=lineNum(), errorFileName=filename())
            self.jsonDict = tmpBackUpDict.copy()
            return False


    def saveJsonFile(self, filePath:str, saveDict:dict) -> None:
        with open(filePath, 'w', encoding=CORE_ENCODING_FORMAT) as wf:
            json.dump(saveDict, wf, indent='\t')


    def getJsonDict(self) -> dict:
        if self.checkJsonDictType() is True:
            return self.jsonDict
        else:
            return {}


    def setAllJsonDict(self, setDict:dict) -> None:
        if str(type(setDict)) == "<class 'dict'>":
            self.jsonDict = setDict.copy()
        else:
            raise ValueError


    def setAddDict(self, addDict:dict) -> bool:
        if not addDict:
            return False
        
        if str(type(addDict)) == "<class 'dict'>":
            for k, v in addDict.items():
                self.jsonDict[k] = v
            return True
        
        else:
            raise ValueError


    def checkJsonDictType(self) -> bool:
        if str(type(self.jsonDict)) != "<class 'dict'>":
            self.jsonDict = {}
            return False
        return True


    def isOverwrittenDict(self, checkDict:dict) -> bool:
        if str(type(checkDict)) != "<class 'dict'>":
            raise ValueError
        
        if not checkDict or not self.jsonDict:
            return False

        isOverwritten = False

        for originEachKey in self.jsonDict.keys():
            for addEachKey in checkDict.keys():
                if originEachKey == addEachKey:
                    showLog(f'- [{originEachKey}] is Overwritten')
                    isOverwritten = True

        return isOverwritten


    def removeDict(self, key:str) -> bool:
        if self.jsonDict.get(key) is None:
            return False
        
        del(self.jsonDict[key])
        return True
    
    
    def editDict(self, originKey:str, editDict:dict) -> bool:
        if str(type(editDict)) != "<class 'dict'>":
            raise ValueError
        
        if str(type(originKey)) != "<class 'str'>":
            raise ValueError
        
        editKey = list(editDict.keys())[0]
        editVal = list(editDict.values())[0]
        
        if self.jsonDict.get(originKey) is None:
            return False
        
        # 바꾸려는 게 키값이라면, 기존 키값 dict 는 제거
        if originKey != editKey:
            self.jsonDict.pop(originKey)
    
        self.jsonDict[editKey] = editVal
        
        return True    


    def getKeyList(self) -> list:
        return list(self.jsonDict.keys())
