# UNIT TEST CODE
# python -m unittest my_test.py
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
import unittest


# SUB IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
import subprocess
import os
import sys
import json
import functools


# Add Import Path
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Core'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))


# Custom Modules
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from Core.JsonManage    import *
from Core.CommonUse     import *
from Core.CodeManage    import *

# Const Define
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
JSON_HEAD = "\n[JsonManage]"
CODE_HEAD = "\n[CodeManage]"
CMMN_HEAD = "\n[CommonUse]"

SHOW_FUNC_HEAD = "\t>"

# Show & Decorate
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
def showHead(HEAD):
    print(HEAD, callername())
    
    
def showFunc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(SHOW_FUNC_HEAD, func.__name__)
        value = func(*args, **kwargs)
        return value
    return wrapper
        

# TestClass : JsonManage
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
class JsonManageTests(unittest.TestCase):
    # UnitTest 맨 처음 시작할 때 구동되는 함수
    @classmethod
    def setUpClass(cls):
        showHead(JSON_HEAD)
        cls.fileName = 'test_JM.json'
        cls.testJson = {   
                            'A':{"Path":"A:\\A", "RunFileName":"mainA.py"},
                            'B':{"Path":"B:\\B", "RunFileName":"mainB.py"},
                            'C':{"Path":"C:\\C", "RunFileName":"mainC.py"}
                        }

        with open(cls.fileName, 'wt') as wf:
            json.dump(cls.testJson, wf, indent="\t")

        cls.JM = JsonManage()
        cls.JM.openJsonFile(cls.fileName)
        cls.jsonDict = cls.JM.getJsonDict()


    # UnitTest 끝날 때 마지막 구동되는 함수
    @classmethod
    def tearDownClass(cls):
        showHead(JSON_HEAD)
        os.remove(cls.fileName)


    @showFunc
    def test_openJsonFile_open_force_wrong_json_file(self):
        wrongPath       = r'./WrongDirectory/JsonFile.json'
        wrongJsonFile   = JsonManage()
        self.assertRaises(Exception, wrongJsonFile.openJsonFile(wrongPath))


    @showFunc
    def test_success_open_json_file_as_path(self):
        PathExtract = self.jsonDict['A']['Path']
        self.assertEqual(PathExtract, "A:\\A")

    @showFunc
    def test_success_open_json_file_as_filename(self):
        FileExtract = self.jsonDict['A']['RunFileName']
        self.assertEqual(FileExtract, "mainA.py")


    @showFunc
    def test_saveJsonFile_correct(self):
        # Save
        saveFileName    = 'test_json_save.json'
        originLen       = len(self.jsonDict)
        self.JM.saveJsonFile(saveFileName, self.jsonDict)

        # Check
        testSavedJM     = JsonManage()
        testSavedJM.openJsonFile(saveFileName)
        testSavedDict   = testSavedJM.getJsonDict()
        loadLen         = len(testSavedDict)

        try:
            os.remove(saveFileName)
        except:
            pass

        self.assertEqual(loadLen, originLen)


    @showFunc
    def test_getJsonDict_correct_dict(self):
        testDict    = self.JM.getJsonDict()
        DictLen     = len(testDict)
        self.assertEqual(DictLen, 3)


    @showFunc
    def test_getKeyList_correct_key_list(self):
        testKeyList = self.JM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C'])


    @showFunc
    def test_getKeyList_empty_key_list(self):
        tmpEmptyJM      = JsonManage({})
        tmpEmptyKeyList = tmpEmptyJM.getKeyList()
        self.assertListEqual(tmpEmptyKeyList, [])


    @showFunc
    def test_setAllJsonDict_new_dict(self):
        tmpJM       = JsonManage(self.jsonDict)

        setNewDict = {   
                        'D':{"Path":"D:\\D", "RunFileName":"mainD.py"},
                        'E':{"Path":"E:\\E", "RunFileName":"mainE.py"},
                        'F':{"Path":"F:\\F", "RunFileName":"mainF.py"}
                    }

        tmpJM.setAllJsonDict(setNewDict)
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['D', 'E', 'F'])


    @showFunc
    def test_setAllJsonDict_check_async(self):
        tmpJM       = JsonManage(self.jsonDict)

        setNewDict = {   
                        'D':{"Path":"D:\\D", "RunFileName":"mainD.py"},
                        'E':{"Path":"E:\\E", "RunFileName":"mainE.py"},
                        'F':{"Path":"F:\\F", "RunFileName":"mainF.py"}
                    }

        tmpJM.setAllJsonDict(setNewDict)
        setNewDict['G'] = {"Path":"G:\\G", "RunFileName":"mainG.py"}
        testKeyList     = tmpJM.getKeyList()
        
        self.assertListEqual(testKeyList, ['D', 'E', 'F'])


    @showFunc
    def test_setAllJsonDict_but_not_dict(self):
        tmpJM = JsonManage(self.jsonDict)
        notDict = [1, 2, 3]
        self.assertRaises(ValueError, lambda:tmpJM.setAllJsonDict(notDict))
        
        
    @showFunc
    def test_setAddDict_but_not_dict(self):
        tmpJM = JsonManage(self.jsonDict)
        notDict = [1, 2, 3]
        self.assertRaises(ValueError, lambda:tmpJM.setAddDict(notDict))


    @showFunc
    def test_setAddDict_but_empty_return_false(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.setAddDict({})
        self.assertFalse(res)


    @showFunc
    def test_setAddDict_but_empty_dict_result(self):
        tmpJM       = JsonManage(self.jsonDict)
        _           = tmpJM.setAddDict({})
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C'])


    @showFunc
    def test_setAddDict_one_result_key(self):
        tmpJM       = JsonManage(self.jsonDict)
        _           = tmpJM.setAddDict({'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C', 'Z'])


    @showFunc
    def test_setAddDict_one_result_value(self):
        tmpJM       = JsonManage(self.jsonDict)
        _           = tmpJM.setAddDict({'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        resDict     = tmpJM.getJsonDict()
        checkValue  = resDict['Z']
        self.assertDictEqual(checkValue, {"Path":"Z:\\Z", "RunFileName":"mainZ.py"})


    @showFunc
    def test_setAddDict_more_one_key(self):
        tmpJM       = JsonManage(self.jsonDict)
        _           = tmpJM.setAddDict({'Y':{"Path":"Y:\\Y", "RunFileName":"mainY.py"},
                                        'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C', 'Y', 'Z' ])


    @showFunc
    def test_checkJsonDictType_create_but_list(self):
        tmpJM   = JsonManage([1,2,3])
        res     = tmpJM.checkJsonDictType()
        self.assertFalse(res)
        
        
    @showFunc
    def test_isOverwrittenDict_but_not_dict(self):
        tmpJM   = JsonManage()
        self.assertRaises(ValueError, lambda:tmpJM.isOverwrittenDict([1, 2, 3]))

    
    @showFunc
    def test_isOverwrittenDict_when_origin_empty(self):
        tmpJM   = JsonManage()
        res     = tmpJM.isOverwrittenDict({'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        self.assertFalse(res)


    @showFunc
    def test_isOverwrittenDict_when_new_empty(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.isOverwrittenDict({})
        self.assertFalse(res)


    @showFunc
    def test_isOverwrittenDict_realOverwritten(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.isOverwrittenDict({'A':'AAA', 'B':'BBB'})
        self.assertTrue(res)
        
        
    @showFunc
    def test_maintain_before_dict_when_wrong_json_open(self):
        tempJM      = JsonManage({'A':'AAA', 'B':'BBB'})
        wrongPath   = r'./WrongDirectory/JsonFile.json'
        tempJM.openJsonFile(wrongPath)
        self.assertDictEqual(tempJM.getJsonDict(), {'A':'AAA', 'B':'BBB'})
        
        
    @showFunc
    def test_load_success_json_when_already_exist_dict(self):
        tempJM      = JsonManage({'D':'AAA', 'E':'BBB'})
        tempJM.openJsonFile(self.fileName)
        tempKeyList = tempJM.getKeyList()
        self.assertListEqual(tempKeyList, ['A', 'B', 'C']) 
        
        
    @showFunc
    def test_removeDict_but_not_exist(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.removeDict('X')
        self.assertFalse(res)
        
        
    @showFunc
    def test_removeDict_correct(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.removeDict('A')
        kList   = tmpJM.getKeyList()
        self.assertTrue(res)
        self.assertListEqual(kList, ['B', 'C'])
        
        
    @showFunc
    def test_editDict_but_not_valid_args(self):
        tmpJM   = JsonManage(self.jsonDict)
        self.assertRaises(ValueError, lambda:tmpJM.editDict("A", [1, 2, 3]))
        self.assertRaises(ValueError, lambda:tmpJM.editDict(1, {'F':{"Path":"F:\\F", "RunFileName":"mainF.py"}}))


    @showFunc
    def test_editDict_but_not_exist_key(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.editDict('F', {'F':{"Path":"F:\\F", "RunFileName":"mainF.py"}})
        self.assertFalse(res)
        
        
    @showFunc
    def test_editDict_change_key(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.editDict('A', {'X':{"Path":"A:\\A", "RunFileName":"mainA.py"}})
        kList   = tmpJM.getKeyList()
        self.assertTrue(res)
        self.assertListEqual(kList, ['B', 'C', 'X'])
        
        
    @showFunc
    def test_editDict_change_value(self):
        tmpJM   = JsonManage(self.jsonDict)
        res     = tmpJM.editDict('A', {'A':{"Path":"X:\\X", "RunFileName":"mainX.py"}})
        chkVal  = tmpJM.getJsonDict()['A']['RunFileName']
        self.assertTrue(res)
        self.assertEqual(chkVal, "mainX.py")       


    @showFunc
    def test_checkValidCreate_run_correct(self):
        res = self.JM.checkValidCreate()
        self.assertTrue(res)




# TestClass : CodeManage
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
class CodeManageTests(unittest.TestCase):
    # UnitTest 맨 처음 시작할 때 구동되는 함수
    @classmethod
    def setUpClass(cls):
        showHead(CODE_HEAD)
        cls.curFilePath = os.path.dirname(os.path.realpath(__file__))
        cls.fileName = 'test_CM.json'
        cls.testJson = {   
                            'A':{"Path":"A:\\A",                "RunFileName":"mainA.py"},
                            'B':{"Path":"B:\\B",                "RunFileName":"mainB.py"},
                            'C':{"Path":f"{cls.curFilePath}",   "RunFileName":"TotalTest.py"}

                        }

        with open(cls.fileName, 'wt') as wf:
            json.dump(cls.testJson, wf, indent="\t")

        cls.CM = CodeManage(cls.fileName)


    # UnitTest 끝날 때 마지막 구동되는 함수
    @classmethod
    def tearDownClass(cls):
        showHead(CODE_HEAD)
        os.remove(cls.fileName)


    @showFunc
    def test_CodeManage_make_class_wrong_json_file(self):
        tmpCM = CodeManage(r'./WrongDirectory/JsonFile.json')
        tmpDict = tmpCM.JM.getJsonDict()
        self.assertDictEqual(tmpDict, {})
        
        
    @showFunc
    def test_getCodeTotalList_empty(self):
        tmpCM = CodeManage(r'./InValid.json')
        tmpList = tmpCM.getCodeTotalList()
        self.assertListEqual(tmpList, [])
        
        
    @showFunc
    def test_getCodeTotalList_correct(self):
        tmpCM = CodeManage(self.fileName)
        tmpList = tmpCM.getCodeTotalList()
        self.assertListEqual(tmpList, [['A', 'A:\\A',               'mainA.py'], 
                                       ['B', 'B:\\B',               'mainB.py'], 
                                       ['C', f'{self.curFilePath}', 'TotalTest.py']])
        
        
    @showFunc
    def test_getCodeAliasesList_empty(self):
        tmpCM = CodeManage(r'./InValid.json')
        tmpList = tmpCM.getCodeAliasesList()
        self.assertListEqual(tmpList, [])        


    @showFunc
    def test_getCodeAliasesList_correct(self):
        tmpCM = CodeManage(self.fileName)
        tmpList = tmpCM.getCodeAliasesList()
        self.assertListEqual(tmpList, ['A', 'B', 'C'])     


    @showFunc
    def test_getCodePathList_empty(self):
        tmpCM = CodeManage(r'./InValid.json')
        tmpList = tmpCM.getCodePathList()
        self.assertListEqual(tmpList, [])        


    @showFunc
    def test_getCodePathList_correct(self):
        tmpCM = CodeManage(self.fileName)
        tmpList = tmpCM.getCodePathList()
        self.assertListEqual(tmpList, ['A:\\A', 'B:\\B', f'{self.curFilePath}'])     


    @showFunc
    def test_getCodeFileNameList_empty(self):
        tmpCM = CodeManage(r'./InValid.json')
        tmpList = tmpCM.getCodeFileNameList()
        self.assertListEqual(tmpList, [])        


    @showFunc
    def test_getCodeFileNameList_correct(self):
        tmpCM = CodeManage(self.fileName)
        tmpList = tmpCM.getCodeFileNameList()
        self.assertListEqual(tmpList, ['mainA.py', 'mainB.py', 'TotalTest.py'])    


    @showFunc
    def test_checkOverwrittenAlreadyUseAlias_realOverwritten(self):
        overWrittenAlias = 'C'
        res = self.CM.checkOverwrittenAlreadyUseAlias(overWrittenAlias)
        self.assertTrue(res)


    @showFunc
    def test_checkOverwrittenAlreadyUseAlias_notOverwritten(self):
        overWrittenAlias = 'D'
        res = self.CM.checkOverwrittenAlreadyUseAlias(overWrittenAlias)
        self.assertFalse(res)
        
        
    @showFunc
    def test_moveTargetDir_not_valid_dir(self):
        wrongDir = r'E://ABCD'
        res = self.CM.moveTargetDir(wrongDir)
        self.assertFalse(res)
        
        
    @showFunc
    def test_moveTargetDir_correct(self):
        originPath  = os.getcwd()
        prePath     = os.path.dirname(os.path.realpath(__file__))
        dest        = os.path.normpath(os.path.join(prePath, './..'))
        _           = self.CM.moveTargetDir(dest)
        curPath     = os.getcwd()
        self.assertEqual(dest, curPath)
        os.chdir(originPath)
        
        
    @showFunc
    def test_getNumByAlias_but_empty_alias(self):
        tmpCM = CodeManage(r'./InValid.json')
        validAlias = 'A'
        resInt = tmpCM.getNumByAlias(validAlias)
        self.assertEqual(resInt, -1)        
        

    @showFunc
    def test_getNumByAlias_wrong_alias(self):
        wrongAlias = 'X'
        resInt = self.CM.getNumByAlias(wrongAlias)
        self.assertEqual(resInt, -1)
        
        
    @showFunc
    def test_getNumByAlias_correct_alias(self):
        validAlias = 'A'
        resInt = self.CM.getNumByAlias(validAlias)
        self.assertEqual(resInt, 0)
        
        validAlias = 'B'
        resInt = self.CM.getNumByAlias(validAlias)
        self.assertEqual(resInt, 1)
        
        
    @showFunc
    def test_checkRealExistFileByAlias_wrong_alias(self):
        res = self.CM.checkRealExistFileByAlias('X')
        self.assertFalse(res)
        

    @showFunc
    def test_checkRealExistFileByAlias_correct_alias(self):
        res = self.CM.checkRealExistFileByAlias('C')
        self.assertTrue(res)



# TestClass : CommonUse
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
class CommonUseTests(unittest.TestCase):
    # UnitTest 맨 처음 시작할 때 구동되는 함수
    @classmethod
    def setUpClass(cls):
        showHead(CMMN_HEAD)
        cls.curPath = os.path.dirname(os.path.abspath(__file__))


    # UnitTest 끝날 때 마지막 구동되는 함수
    @classmethod
    def tearDownClass(cls):
        showHead(CMMN_HEAD)

        
    @showFunc
    def test_check_func_name_show(self):
        fncName = funcname()
        self.assertEqual(fncName, "test_check_func_name_show")
        
        
    @showFunc
    def test_check_caller_name_show(self):
        clrName = callername(3)
        self.assertEqual(clrName, "_callTestMethod")
        
        
    @showFunc
    def test_check_file_name_show(self):
        fileName = filename()
        self.assertEqual(fileName, "TotalTest")
        
        
    @showFunc
    def test_check_valid_isTrue(self):
        res = isTrue(False)
        self.assertFalse(res)
        
        
    @showFunc
    def test_setResultDir_if_already_exist(self):
        res = setResultDir(self.curPath)
        self.assertTrue(res)
        
        
    @showFunc
    def test_setResultDir_if_none_exist(self):
        TestDirPath = os.path.join(self.curPath, 'TestDir')
        res         = setResultDir(TestDirPath)
        os.removedirs(TestDirPath)
        self.assertFalse(res)
        
        
    @showFunc
    def test_correct_read_n_write_to_list(self):
        TestFilePath    = os.path.join(self.curPath, 'TestRWFile.txt')
        TestWriteList   = ['a', 'b', 'c']
        TestReadList    = []
        writeListToFile(TestFilePath, TestWriteList)
        readFileToList(TestFilePath, TestReadList)
        
        if os.path.isfile(TestFilePath):
            os.remove(TestFilePath)
            
        self.assertListEqual(TestReadList, ['a', 'b', 'c'])
        
        
def showOffLog():
    print("# SHOW OFF LOG")
    setCoreValue('CORE_SHOW_LOG', False)


if __name__ == "__main__":
    showOffLog()
    unittest.main()
    