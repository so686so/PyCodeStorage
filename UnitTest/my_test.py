import unittest

# SUB IMPORT
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
import subprocess
import os
import sys
import json

# Add Import Path
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../Core'))

# Custom Modules
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
from JsonManage             import *
from CommonUse              import *

# 할 거 -> json 읽는 경우 전부 테스트 만들기 : 파일 없을 때 / 파일 있지만 목록 없을 때
# python -m unittest my_test.py

CodeListDict = {}

class CodeStorageTests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('>>', funcname())
        cls.fileName = 'test_json.json'
        cls.testJson = {   
                            'A':{"Path":"A:\\A", "RunFileName":"mainA.py"},
                            'B':{"Path":"B:\\B", "RunFileName":"mainB.py"},
                            'C':{"Path":"C:\\C", "RunFileName":"mainC.py"}
                        }

        with open(cls.fileName, 'wt') as f:
            json.dump(cls.testJson, f, indent="\t")

        cls.JM = JsonManage()
        cls.JM.openJsonFile(cls.fileName)
        cls.jsonDict = cls.JM.getJsonDict()


    @classmethod
    def tearDownClass(cls):
        print('>>', funcname())
        try:
            os.remove(cls.fileName)
        except:
            pass


# JsonManage UnitTest
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    def test_open_force_wrong_json_file(self):
        print('\t>', funcname())
        wrongPath = r'./WrongDirectory/JsonFile.json'
        wrongJsonFile = JsonManage()
        self.assertRaises(Exception, wrongJsonFile.openJsonFile(wrongPath))


    def test_success_open_json_file_as_path(self):
        print('\t>', funcname())
        PathExtract = self.jsonDict['A']['Path']
        self.assertEqual(PathExtract, "A:\\A")


    def test_success_open_json_file_as_filename(self):
        print('\t>', funcname())
        FileExtract = self.jsonDict['A']['RunFileName']
        self.assertEqual(FileExtract, "mainA.py")


    def test_json_file_save(self):
        print('\t>', funcname())
        saveFileName = 'test_json_save.json'

        self.JM.saveJsonFile(saveFileName, self.jsonDict)

        testSavedJM = JsonManage()
        testSavedJM.openJsonFile(saveFileName)
        testSavedDict = testSavedJM.getJsonDict()
        DictLen = len(testSavedDict)

        try:
            os.remove(saveFileName)
        except:
            pass

        self.assertEqual(DictLen, 3)


    def test_json_get_correct_dict(self):
        print('\t>', funcname())
        testDict = self.JM.getJsonDict()
        DictLen = len(testDict)
        self.assertEqual(DictLen, 3)


    def test_json_get_correct_key_list(self):
        print('\t>', funcname())
        testKeyList = self.JM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C'])


    def test_json_get_empty_key_list(self):
        print('\t>', funcname())
        tmpEmptyJM = JsonManage()
        tmpEmptyKeyList = tmpEmptyJM.getKeyList()
        self.assertListEqual(tmpEmptyKeyList, [])


    def test_json_set_all_new_dict(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)

        setNewDict = {   
                        'D':{"Path":"D:\\D", "RunFileName":"mainD.py"},
                        'E':{"Path":"E:\\E", "RunFileName":"mainE.py"},
                        'F':{"Path":"F:\\F", "RunFileName":"mainF.py"}
                    }

        tmpJM.setAllJsonDict(setNewDict)
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['D', 'E', 'F'])


    def test_set_add_dict_but_empty_return_false(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.setAddDict({})
        self.assertFalse(res)


    def test_set_add_dict_but_empty_dict_result(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.setAddDict({})
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C'])


    def test_set_add_dict_one_result_key(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.setAddDict({'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C', 'Z'])


    def test_set_add_dict_one_result_value(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.setAddDict({'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        resDict = tmpJM.getJsonDict()
        checkValue = resDict['Z']
        self.assertDictEqual(checkValue, {"Path":"Z:\\Z", "RunFileName":"mainZ.py"})


    def test_set_add_dict_more_one_key(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.setAddDict({'Y':{"Path":"Y:\\Y", "RunFileName":"mainY.py"}, 'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        testKeyList = tmpJM.getKeyList()
        self.assertListEqual(testKeyList, ['A', 'B', 'C', 'Y', 'Z' ])


    def test_jsonManage_create_arg_list(self):
        print('\t>', funcname())
        tmpJM = JsonManage([1,2,3])
        res = tmpJM.checkJsonDictType()
        self.assertFalse(res)

    
    def test_isOverwrittenDict_when_origin_empty(self):
        print('\t>', funcname())
        tmpJM = JsonManage()
        res = tmpJM.isOverwrittenDict({'Z':{"Path":"Z:\\Z", "RunFileName":"mainZ.py"}})
        self.assertFalse(res)


    def test_isOverwrittenDict_when_new_empty(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.isOverwrittenDict({})
        self.assertFalse(res)


    def test_isOverwrittenDict_realOverwritten(self):
        print('\t>', funcname())
        tmpJM = JsonManage(self.jsonDict)
        res = tmpJM.isOverwrittenDict({'A':'AAA', 'B':'BBB'})
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()