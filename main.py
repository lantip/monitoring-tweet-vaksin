import twint
import requests
import json
import shutil

def download_tweets():
    total = []

    tweets = []
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

result = download_tweets()

if result:
    fle = open('twit.json','r').read()

    data = json.loads(fle)

    for dat in data:
        for foto in dat['photos']:
            r = requests.get(foto, verify=False, stream=True)
            if r.status_code == 200:
                with open('data/'+dat['datestamp']+'.jpg', 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)  