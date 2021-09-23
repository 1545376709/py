#!/usr/bin/python
import json
import re

import requests
import get_mp3_mp4_path as ph


def main():
    url = 'https://www.bilibili.com/v/knowledge/campus/#/'
    download_videos_num_size_set(url, 100, 100)


#     取得mp3，mp4，下载链接
# mp3_path, mp4_path = ph.get_mp3_and_mp4_path(url)


def download_videos_num_size_set(url, num, size):
    #        指定下载url：url
    #        下载数量：num
    #        视频大小：size，MB为单位
    if url == '':
        return ''
    hot_rank_url = 'https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video' \
                   '&view_type=hot_rank' \
                   '&order=click&copy_right=-1' \
                   '&cate_id=208' \
                   '&page=1' \
                   '&pagesize=20&jsonp=jsonp' \
                   '&time_from=20210914&time_to=20210921&callback=jsonCallback_bili_45958586295567143'
    url = 'https://api.bilibili.com/x/web-interface/newlist?rid=208&type=0&pn=1&ps=100&jsonp=jsonp&callback' \
          '=jsonCallback_bili_29618727244170222 '
    headers = {
        'Referer': 'https://www.bilibili.com/v/knowledge/campus/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 '
    }
    print(headers["User-Agent"])
    print(hot_rank_url)
    return 0
    resp = requests.get(url, headers=headers)
    print(resp.text)

    json_str = re.sub('jsonCallback_bili_.*?\(', '', resp.text)
    print(re.sub('jsonCallback_bili_.*?\(', '', resp.text))
    json_str = json_str[:-1]
    print(json_str)
    jsons = json.loads(json_str)
    print(jsons)
    results = jsons["data"]["archives"]
    print(results)
    for result in results:
        href = 'https://www.bilibili.com/video/{}'.format(result['bvid'])
        print(href)
    #     开始下载视频
        download_video(href)



    if resp.status_code != 206:
        return resp.status_code
        print(resp.status_code)
        print(resp.text)

    return 0


if __name__ == '__main__':
    main()


def download_video(href):
    headers = {
        'Referer': 'https://www.bilibili.com/v/knowledge/campus/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36 '
    }