#!/usr/bin/python
import json
import os
import re
import urllib3

import requests

import download
import download_mp4_mp3
import value


def download_mp4(url):
    return


def main():
    download_videos_num_size_set()


def download_videos_num_size_set():
    hot_rank_url = 'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order' \
                   '=click&copy_right=1' \
                   '&cate_id={}' \
                   '&page=1' \
                   '&pagesize={}' \
                   '&jsonp=jsonp' \
                   '&time_from={}' \
                   '&time_to={}'.format(value.tag_id, value.download_num, value.time_from, value.time_to)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 '
    }

    resp = requests.get(hot_rank_url, headers=headers)

    # json_str = re.sub('jsonCallback_bili_.*?\(', '', resp.text)
    # print(re.sub('jsonCallback_bili_.*?\(', '', resp.text))
    # json_str = json_str[:-1]  # 截去最后一个字符
    # print(json_str)
    # jsons = json.loads(json_str)

    # print(resp.text)
    # print(resp.headers.get('Content-Length'))
    jsons = json.loads(resp.text)
    # print(jsons)
    results = jsons["result"]
    # print(results)
    for result in results:
        href = 'https://www.bilibili.com/video/{}'.format(result['bvid'])
        print(href)
        #     开始下载视频
        # download_video(href)
        # try:
        download.download_video(href)
    # except:
    #     print('fail to download')
    #     pass


def get_mp3_mp4_url(href):
    if href == '':
        # href = 'https://www.bilibili.com/video/BV1Gq4y1f7U7'
        href = 'https://www.bilibili.com/video/BV1bU4y1P7VG'
    headers = {
        'host': 'www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 ',
        'Cookie': 'b_ut=-1; i-wanna-go-back=1; _uuid=2A21F6F7-DBB3-C790-1633-7F749D844BE730769infoc; '
                  'buvid3=3249A35D-3C25-44C2-BD1E-ABE85CBCB7B6167643infoc; b_nut=1632238231; PVID=2; '
                  'CURRENT_FNVAL=80; blackside_state=1; rpdid=|(kJYRlRmYYm0J\'uYJkkRR)lR; '
                  'LIVE_BUVID=AUTO2016323805367877; fingerprint=1d1a3709c110784753b2bd9022fbc756; '
                  'buvid_fp=3249A35D-3C25-44C2-BD1E-ABE85CBCB7B6167643infoc; '
                  'buvid_fp_plain=3ED42C55-C92D-4DE7-AB11-4E48AF9B1533148793infoc; DedeUserID=361401613; '
                  'DedeUserID__ckMd5=2fe28fbf34c9128b; SESSDATA=045accfd%2C1648021978%2Cab73a*91; '
                  'bili_jct=26105a0aacb6424409a78a2fbe6e99ea; innersign=1; bsource=search_baidu; sid=blxz47qm; '
                  'CURRENT_QUALITY=112 '
    }
    resp = requests.get(href, headers=headers)
    # print(resp.text)
    json_str = resp.text.split('window.__playinfo__=')[-1].split('<')[0].split(';')[0]
    jsons = json.loads(json_str)
    print(jsons)
    if jsons["data"]["dash"]:
        videos = jsons["data"]["dash"]["video"]
        audios = jsons["data"]["dash"]["audio"]
        for video in videos:
            if video["codecs"] == 'hev1.1.6.L120.90':
                continue
            print(video["baseUrl"])
            print(video["codecs"])
            get_content_length(video["baseUrl"])
            # download_mp4_mp3.download_mp3_mp4('', video["baseUrl"], 'dance{}'.format(video["bandwidth"]))
            # break
            # if download(video["baseUrl"]):
            #     break
        mp4_url = jsons["data"]["dash"]["video"][0]["baseUrl"]
        mp3_url = jsons["data"]["dash"]["audio"][0]["baseUrl"]

    data = jsons["data"]
    return


def get_content_length(url):
    headers = {
        'Range': 'bytes={}-{}'.format(0, 100),
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(url, headers=headers, verify=False)
    print(resp.headers.get('content-range'))
    return


if __name__ == '__main__':
    try:
        os.mkdir('./videos')
        os.mkdir('./audios')
        os.mkdir('./infos')
        os.mkdir('./pics')
        os.mkdir('./MP4')
    except:
        pass
    urllib3.disable_warnings()
    main()
    # get_mp3_mp4_url('')
