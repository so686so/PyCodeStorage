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
from JsonManage             import *
from CommonUse              import *

# Refer to CoreDefine.py
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from CoreDefine import *


# JsonManage Class
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
class JsonManage:
    def __init__(self, initDict={}):
        self.jsonPath = r''
        self.jsonDict = initDict.copy()


    def checkValidCreate(self):
        self.checkJsonDictType()


    def openJsonFile(self, filePath):
        # try 실패 대비해서 백업하고나서 클리어
        tmpBackUpDict = self.jsonDict
        self.jsonDict.clear()

        try:
            with open(filePath, 'r') as f:
                self.jsonDict = json.load(f)

        except Exception as e:
            print(f'[openJsonFile] -> {e}')
            self.jsonDict = tmpBackUpDict


    def saveJsonFile(self, filePath, saveDict):
        with open(filePath, 'w', encoding=CORE_ENCODING_FORMAT) as wf:
            json.dump(saveDict, wf, indent='\t')


    def getJsonDict(self):
        return self.jsonDict


    def setAllJsonDict(self, setDict):
        self.jsonDict = setDict


    def setAddDict(self, addDict):
        if not addDict:
            return False

        for k, v in addDict.items():
            self.jsonDict[k] = v

        return True


    def checkJsonDictType(self):
        if str(type(self.jsonDict)) != "<class 'dict'>":
            self.jsonDict = {}
            return False
        return True


    def isOverwrittenDict(self, checkDict):
        if not checkDict or not self.jsonDict:
            return False

        isOverwritten = False

        for originEachKey in self.jsonDict.keys():
            for addEachKey in checkDict.keys():
                if originEachKey == addEachKey:
                    print(f'- [{originEachKey}] is Overwritten')
                    isOverwritten = True

        return isOverwritten


    # dict 제거
    # dict 키값 있는지 체크하는 것


    def getKeyList(self):
        return list(self.jsonDict.keys())
