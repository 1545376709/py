import os

import requests
import get_mp3_mp4_path as ph


def download_mp4(min, max, url, title):
    if url == '':
        return ''
    headers = {
        'Range': 'bytes={}-{}'.format(min, max),
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


def download_mp3(min, max, url, title):
    # 如果没有音频
    if url == '':
        return ''
    headers = {
        'Range': 'bytes={}-{}'.format(min, max),
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 206:
        return resp.status_code
    print(resp.status_code)
    # print(resp.text)
    with open('audios/{}.mp3'.format(title), 'ab+') as f:
        f.write(resp.content)
    return 0


def download_mp3_mp4(mp3_path, mp4_path, title):
    min = 0
    # max = 200000
    max = 85000000
    mp4_status_code = 0
    mp3_status_code = 0
    while True:
        if mp4_status_code == 0:
            mp4_status_code = download_mp4(min, max, mp4_path, title)
            print("mp4_status_code:", mp4_status_code)
        else:
            pass
        if mp3_status_code == 0:
            mp3_status_code = download_mp3(min, max, mp3_path, title)
            print('mp3_status_code:', mp3_status_code)
        else:
            pass
        if mp4_status_code != 0 and mp3_status_code != 0:
            break
        min = max + 1
        max = max + 200000


def main():
    url = 'https://www.bilibili.com/video/BV1X5411x75s'
    mp4_path = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/69/49/412434969/412434969-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632306715&gen=playurlv2&os=cosbv&oi=3704121609&trid=36c9705a5e504b4dabf76e12f264e630u&platform=pc&upsig=47c1f959083bcd79bf6040f2d7b3a280&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=1&logo=80000000'
    mp3_path = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/69/49/412434969/412434969-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632306715&gen=playurlv2&os=cosbv&oi=3704121609&trid=36c9705a5e504b4dabf76e12f264e630u&platform=pc&upsig=1a467c72cecc6a5cde96a27ce16f05bc&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=1&logo=80000000'
    title = 'test'

    # mp3_path, mp4_path = ph.get_mp3_and_mp4_path(url)
    print(mp4_path)
    title = 'test'
    os.mkdir('./videos')
    os.mkdir('./audios')
    download_mp3_mp4(mp3_path, mp4_path, title)
    # print(os.curdir)


if __name__ == '__main__':
    main()
