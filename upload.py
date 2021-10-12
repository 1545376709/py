import json
import os
import requests
from requests_toolbelt import MultipartEncoder


def main():
    upload_url = 'http://localhost:8080/upload_test'
    for f in os.listdir('f'):
        if f.find('.json') > 0:
            jso = json.load(open('f/{}'.format(f), 'r', encoding='utf-8'))
            print(jso)
            files = {'file': open('f/{}.mp4'.format(jso["bvid"]), 'rb'),
                     'pic': open('f/{}.jpg'.format(jso["bvid"]), 'rb'),
                     }
            m = MultipartEncoder(files)
            resp = requests.post(upload_url, m, headers={'Content-Type': m.content_type})
            print(resp.text)


if __name__ == '__main__':
    main()
