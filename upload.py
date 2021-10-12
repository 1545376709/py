import json
import os
import requests


def main():
    upload_url = 'localhost:8081/dev/upload'
    for f in os.listdir('f'):
        if f.find('.json') > 0:
            jso = json.load(open('f/{}'.format(f), 'r', encoding='utf-8'))
            print(jso)
            files = {'file': open('f/{}.mp4'.format(jso["bvid"]), 'rb'),
                     'pic': open('f/{}.jpg'.format(jso["bvid"]), 'rb')
                     }
            resp = requests.post(upload_url, files, jso)


if __name__ == '__main__':
    main()
