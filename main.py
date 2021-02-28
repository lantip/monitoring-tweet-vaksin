import twint
import requests
import json
import shutil
import dateparser

from os import walk
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def download_tweets():
    total = []
    f = []
    for (dirpath, dirnames, filenames) in walk(dir_path+'/data'):
        f.extend(filenames)
        break
    dte = None
    for filenames in f:
        if not dte:
            dte = dateparser.parse(filenames.replace('.jpg', ''))
        else:
            dtes = dateparser.parse(filenames.replace('.jpg', ''))
            if dtes > dte:
                dte = dtes

    tweets = []
    '''
    #search twit KemenkesRI. Berhenti tanggal 25 Februari 2021
    c = twint.Config()
    c.Username = 'KemenkesRI'
    c.Search = 'update perkembangan vaksinasi'
    c.Images = True
    c.Store_object = True
    c.Store_object_tweets_list = tweets
    twint.run.Search(c)

    for twt in tweets:
        total.append(twt.__dict__)

    with open('twit.json', 'w') as fle:
        fle.write(json.dumps(total, indent=4))
    return total
    '''

    #search twit BNPB  https://twitter.com/bnpb_indonesia/status/1365587433677488128?s=21
    c = twint.Config()
    c.Username = 'bnpb_indonesia'
    c.Search = 'Update percepatan #BersatuLawanCovid19'
    c.Since = dte.strftime('%Y-%m-%d')
    c.Images = True
    c.Store_object = True
    c.Store_object_tweets_list = tweets
    twint.run.Search(c)

    for twt in tweets:
        total.append(twt.__dict__)

    with open('twit-bnpb.json', 'w') as fle:
        fle.write(json.dumps(total, indent=4))
    return total
result = download_tweets()

if result:
    fle = open('twit-bnpb.json','r').read()

    data = json.loads(fle)

    for dat in data:
        for idx, foto in enumerate(dat['photos']):
            if idx < 1:
                r = requests.get(foto, verify=False, stream=True)
                if r.status_code == 200:
                    if not os.path.isfile('data/'+dat['datestamp']+'.jpg'):
                        with open('data/'+dat['datestamp']+'.jpg', 'wb') as f:
                            r.raw.decode_content = True
                            shutil.copyfileobj(r.raw, f)  