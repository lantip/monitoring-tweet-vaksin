from PIL import Image, ImageOps
from pytesseract import image_to_string
#from ocr_kemenkes import ocr_date  #versi kemenkes berhenti sejak 25 Februari 2021
from ocr_bnpb import ocr_date
import json
from os import walk
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

f = []
for (dirpath, dirnames, filenames) in walk(dir_path+'/data'):
    f.extend(filenames)
    break
try:
    result = json.loads(open('result.json','r').read())
except:
    result = []
dates = []
for res in result:
    dates.append(res['date'])

for i in f:
    if not i.replace('.jpg','') in dates:
        rslt = ocr_date(i)
        if rslt:
            rslt['date'] = i.replace('.jpg','')
            result.append(rslt)

#result = hasil.items()
#sorted_result = sorted(result)
#hasil = ocr_date('2020-05-09.jpg')
newlist = sorted(result, key=lambda k: k['date']) 

with open('result.json','w') as fle:
    fle.write(json.dumps(newlist,indent=4))

print(json.dumps(newlist,indent=4))