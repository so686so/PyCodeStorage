import subprocess
import os
import json

from Core.JsonManage import JsonManage
from CoreDefine import *


PATH = r''

CodeListDict = {}


json = JsonManage()
json.openJsonFile(JSON_PATH)
CodeListDict = json.getJsonDict()

ChoiceProgram = 'AttributeProgram'

PATH = CodeListDict[ChoiceProgram]['Path']
FILE = CodeListDict[ChoiceProgram]['RunFileName']

print(f'START : {PATH} -> {FILE}')
os.chdir(PATH)
a = subprocess.run(f'python {FILE}')
