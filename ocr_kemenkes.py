from PIL import Image, ImageOps
from pytesseract import image_to_string
import json
from os import walk
import os

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

    if "REGISTRASI ULANG" in lines:
        if "UPDATE VAKSINASI" in lines[1]:
            result['total_sasaran'] = lines[4].split()[1].replace('.','')
            result['sasaran_sdmk'] = lines[7].replace('.','')
            result['registrasi_ulang'] = lines[9].replace('.','')
            if 'TAHAP' in lines[11]:
                tahap = lines[12].split()
                result['tahap_1'] = tahap[0].replace('.','')
                result['tahap_2'] = tahap[1].replace('.','')
            else:
                tahap = lines[11].split()
                result['tahap_1'] = tahap[0].replace('.','')
                result['tahap_2'] = tahap[1].replace('.','')
        else:
            result['total_sasaran'] = lines[0].replace('.','')
            result['sasaran_sdmk'] = lines[3].replace('.','')
            result['registrasi_ulang'] = lines[5].replace('.','')
            tahap = lines[8].split()
            result['tahap_1'] = tahap[0].replace('.','')
            result['tahap_2'] = tahap[1].replace('.','')

    else:
        try:
            stp = int(lines[3].replace('.',''))
        except:
            stp = None
        if stp:
            result['total_sasaran'] = lines[3].replace('.','')
            result['sasaran_sdmk'] = lines[6].replace('.','')
            tahap = lines[9].split()
            result['penambahan_tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
            result['penambahan_tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
            tahap = lines[10].split()
            result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
            result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
            tahap = lines[13].split()
            result['cakupan_tahap_1'] = tahap[0]
            result['cakupan_tahap_2'] = tahap[1]

            return result

        if 'VAKSINASI' in lines[5]:
            result['total_sasaran'] = lines[6].replace('.','')
            result['sasaran_sdmk'] = lines[9].replace('.','')
            tahap = lines[11].split()
            result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
            result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
            tahap = lines[14].split()
            result['cakupan_tahap_1'] = tahap[0]
            result['cakupan_tahap_2'] = tahap[1]
        else:
            if 'VAKSINAS' in lines[0]:
                result['total_sasaran'] = lines[6].replace('.','')
                result['sasaran_sdmk'] = lines[9].replace('.','')
                result['penambahan_tahap_1'] = lines[1].replace('(','').replace(')','').replace('+','').replace('.','')
                result['penambahan_tahap_2'] = lines[12].replace('(','').replace(')','').replace('+','').replace('.','')
                
                result['tahap_1'] = lines[2].replace('(','').replace(')','').replace('+','').replace('.','')
                result['tahap_2'] = lines[13].replace('(','').replace(')','').replace('+','').replace('.','')
                
                result['cakupan_tahap_1'] = lines[5]
                result['cakupan_tahap_2'] = lines[16]

            else:
                start = lines[0].replace('.','')
                try:
                    istart = int(start)
                except:
                    istart = 0
                if istart > 0:
                    if not 'CAKUPAN VAKSINASI CAKUPAN VAKSINASI' in lines[8]:
                        if len(lines) > 11:
                            if len(lines[6].split()) < 2 and '(' in lines[6]:
                                result['total_sasaran'] = istart
                                result['sasaran_sdmk'] = lines[3].replace('.','')
                                result['penambahan_tahap_1'] = lines[6].replace('(','').replace(')','').replace('+','').replace('.','')
                                result['penambahan_tahap_2'] = lines[8].replace('(','').replace(')','').replace('+','').replace('.','')
                                tahap = lines[7].split()
                                result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                                result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                                tahap = lines[11].split()
                                result['cakupan_tahap_1'] = tahap[0]
                                result['cakupan_tahap_2'] = tahap[1]
                            else:
                                result['total_sasaran'] = istart
                                result['sasaran_sdmk'] = lines[3].replace('.','')
                                tahap = lines[6].split()
                                result['penambahan_tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                                result['penambahan_tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                                tahap = lines[7].split()
                                result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                                result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                                tahap = lines[12].split()
                                result['cakupan_tahap_1'] = tahap[0]
                                result['cakupan_tahap_2'] = tahap[1]
                        else:
                            result['total_sasaran'] = istart
                            result['sasaran_sdmk'] = lines[3].replace('.','')
                            tahap = lines[5].split()
                            result['penambahan_tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                            result['penambahan_tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                            tahap = lines[6].split()
                            result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                            result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                            tahap = lines[9].split()
                            result['cakupan_tahap_1'] = tahap[0]
                            result['cakupan_tahap_2'] = tahap[1]
                    else:
                        if 'VAKSINAS!' in lines[4]:
                            result['total_sasaran'] = istart
                            result['sasaran_sdmk'] = lines[3].replace('.','')
                            tahap = lines[6].split()
                            result['penambahan_tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                            result['penambahan_tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                            tahap = lines[7].split()
                            result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                            result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                            tahap = lines[10].split()
                            result['cakupan_tahap_1'] = tahap[0]
                            result['cakupan_tahap_2'] = tahap[1]
                        else:
                            result['total_sasaran'] = istart
                            result['sasaran_sdmk'] = lines[3].replace('.','')
                            result['penambahan_tahap_1'] = lines[5].replace('(','').replace(')','').replace('+','').replace('.','')
                            result['penambahan_tahap_2'] = lines[6].replace('(','').replace(')','').replace('+','').replace('.','')
                            tahap = lines[7].split()
                            result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                            result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                            tahap = lines[10].split()
                            result['cakupan_tahap_1'] = tahap[0]
                            result['cakupan_tahap_2'] = tahap[1]
                else:
                    result['total_sasaran'] = lines[5].replace('.','')
                    result['sasaran_sdmk'] = lines[8].replace('.','')
                    if '(+' in lines[11]:
                        tahap = lines[11].split()
                        result['penambahan_tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                        result['penambahan_tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                        tahap = lines[12].split()
                        result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                        result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                        tahap = lines[15].split()
                        result['cakupan_tahap_1'] = tahap[0]
                        result['cakupan_tahap_2'] = tahap[1]
                    else:
                        tahap = lines[10].split()
                        result['tahap_1'] = tahap[0].replace('(','').replace(')','').replace('+','').replace('.','')
                        result['tahap_2'] = tahap[1].replace('(','').replace(')','').replace('+','').replace('.','')
                        tahap = lines[13].split()
                        result['cakupan_tahap_1'] = tahap[0]
                        result['cakupan_tahap_2'] = tahap[1]
        
    return result
