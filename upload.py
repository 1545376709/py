import json
import os
import requests
from requests_toolbelt import MultipartEncoder


def main():
    upload_url = 'http://localhost:8081/upload_test/8/2'
    for f in os.listdir('infos1'):
        if f.find('.json') > 0:
            jso = json.load(open('infos1/{}'.format(f), 'r', encoding='utf-8'))
            for s in jso:
                jso[s] = str(jso[s])
            jso['file'] = ('MP4/{}.mp4'.format(jso["bvid"]), open('MP4/{}.mp4'.format(jso["bvid"]), 'rb'))
            jso['pic'] = ('pics/{}.jpg'.format(jso["bvid"]), open('pics/{}.jpg'.format(jso["bvid"]), 'rb'))

            m = MultipartEncoder(jso)
            print(jso['bvid'])
            resp = requests.post(upload_url, m, headers={'Content-Type': m.content_type})
            print(resp.text, jso["bvid"])


if __name__ == '__main__':
    main()
