import json

import requests
import download_mp4_mp3


def main():
    # url = 'https://www.bilibili.com/video/BV1X5411x75s'
    # url = 'https://www.bilibili.com/video/BV1Wq4y1o7sf'
    url = 'https://www.bilibili.com/video/BV1Gq4y1f7U7'
    download_video(url)


def download_video(href):
    headers = {
        'host': 'www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 '
    }
    resp = requests.get(href, headers=headers)
    print(resp.text)
    json_str = resp.text.split('window.__playinfo__=')[-1].split('<')[0].split(';')[0]
    jsons = json.loads(json_str)
    print(jsons)
    if jsons["data"]["dash"]:
        mp4_url = jsons["data"]["dash"]["video"][0]["baseUrl"]
        mp3_url = jsons["data"]["dash"]["audio"][0]["baseUrl"]

    data = jsons["data"]
    try:
        dash = data['dash']
        videos = dash['video']
        audios = dash['audio']
        mp3_path = audios[0]['baseUrl']
        mp4_path = videos[0]['baseUrl']
    except:
        mp4_path = ''
        urls = data['durl']
        for url in urls:
            if url['order'] == 1:
                mp4_path = url['url']
    print(mp4_url)
    print(mp3_url)
    print(mp4_path)
    # download_mp4_mp3.download_mp3_mp4(mp4_url, mp3_url, 'dance')


if __name__ == '__main__':
    main()
