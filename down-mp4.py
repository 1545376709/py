#!/usr/bin/python
import requests
import get_mp3_mp4_path as ph

def download_mp4(min,max,url,title):
    if url == '':
        return ''
    headers = {
        'Range': 'bytes={}-{}'.format(min,max),
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 206:
        return resp.status_code
    # print(resp.text)
    print(resp.status_code)
    with open('videos/{}.mp4'.format(title), 'ab+') as f:
        f.write(resp.content)
    return 0

def download_mp3(min,max,url,title):
    # 如果没有音频
    if url == '':
        return ''
    headers = {
        'Range': 'bytes={}-{}'.format(min,max),
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(url,headers = headers)
    if resp.status_code != 206:
        return resp.status_code
    print(resp.status_code)
    # print(resp.text)
    with open('audios/{}.mp3'.format(title),'ab+') as f:
        f.write(resp.content)
    return 0
def download_mp3_mp4(mp3_path, mp4_path,title):
    min = 0
    max = 200000
    mp4_status_code = 0
    mp3_status_code = 0
    while True:
        if mp4_status_code == 0:
            mp4_status_code = download_mp4(min, max,mp4_path,title)
            print("mp4_status_code:",mp4_status_code)
        else:
            pass
        if mp3_status_code == 0:
            mp3_status_code = download_mp3(min, max,mp3_path,title)
            print('mp3_status_code:',mp3_status_code)
        else:
            pass
        if mp4_status_code != 0 and mp3_status_code != 0:
            break
        min = max + 1
        max = max + 200000
def main():
    url = 'https://www.bilibili.com/video/BV1X5411x75s'
    mp3_path, mp4_path = ph.get_mp3_and_mp4_path(url)
    print(mp4_path)
    title = 'test'
    download_mp3_mp4(mp3_path, mp4_path, title)

if __name__ == '__main__':
    main()