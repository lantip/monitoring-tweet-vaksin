from PIL import Image, ImageOps
from pytesseract import image_to_string
import json
from os import walk
import os, re

dir_path = os.path.dirname(os.path.realpath(__file__))

def ocr_date(jpg):
    #ocr untuk twit dari KemenkesRI. berhenti sejak 25 Februari 2021
    im = Image.open(dir_path+'/data/'+jpg)
    im_invert = ImageOps.invert(im)
    img = im_invert.convert('LA')
    data = image_to_string(img)
    result = {}
    lins = data.split('\n')
    lines = []
    for lin in lins:
        if len(lin.strip()) > 1:
            lines.append(lin)    
    
    lne = lines[10].split()
    tahap = []
    for thp in lne:
        cdgt = re.findall(r'\d+', thp)
        if len(cdgt) > 0:
            tahap.append(cdgt)
    ssr = lines[11].split(' | ')
    
    result['total_sasaran'] = ssr[1].replace('.','').replace(' ','')
    result['sasaran_sdmk'] = ssr[0].replace('.','').replace(' ','')
    for idx, val in enumerate(tahap):
        thps = ''.join(val)
        result['penambahan_tahap_'+str(idx+1)] = thps.replace(' ','')
    result['tahap_1'] = ssr[2].replace('(','').replace(')','').replace('+','').replace('.','').replace(' ','')
    result['tahap_2'] = ssr[3].replace('(','').replace(')','').replace('+','').replace('.','').replace(' ','')

    return result
