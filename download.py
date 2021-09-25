#!/usr/bin/python

import json
import re
import requests

import download_mp4_mp3
import value


def download_video(href):
    if href == '':
        href = 'https://www.bilibili.com/video/BV1Gq4y1f7U7'
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
    # print(jsons)

    info_str = resp.text.split('window.__INITIAL_STATE__=')[-1].split('(function')[0].split(';')[0]  # 注意 0 1 -1 的意义

    # print(info_str)
    info_json = json.loads(info_str)

    bvid = info_json["bvid"]

    videoData = info_json["videoData"]

    videoData["desc"] += "\n转载自bilibili" + '\n网址：https://www.bilibili.com/' + bvid

    pic_url = info_json["videoData"]["pic"]

    # title = videoData["title"]

    # desc = videoData["desc"] + "\n转载自bilibili" + '\n网址：https://www.bilibili.com/' + bvid

    # print(desc)

    # print(pic_url)

    if jsons["data"]["dash"]:
        videos = jsons["data"]["dash"]["video"]
        mp3_url = jsons["data"]["dash"]["audio"][0]["baseUrl"]
        for video in videos:
            print(video["baseUrl"])
            if download_mp3_mp4(mp3_url, video["baseUrl"], bvid) == 0:
                # 写入视频信息
                json.dump(videoData, open('infos/{}.json'.format(bvid), 'w', encoding='utf-8'), ensure_ascii=False)

                # 写入视频封面
                headers = {
                    'Referer': 'https://www.bilibili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
                }
                resp = requests.get(pic_url, headers=headers)

                with open('pics/{}.jpg'.format(bvid), 'wb') as f:
                    f.write(resp.content)

                # 合并MP3与MP4
                import subprocess
                try:
                    # subprocess.call('echo 123', shell=True)
                    subprocess.call('ffmpeg -i ' + 'videos/{}.mp4'.format(bvid) + ' -i ' + 'audios/{}.mp3'.format(
                        bvid) + ' -vcodec copy -acodec copy ' + 'MP4/{}.mp4'.format(bvid),
                                    shell=True)
                except:
                    pass
                break

            # download_mp4_mp3.download_mp3_mp4('', video["baseUrl"], 'dance{}'.format(video["bandwidth"]))
            # break
            # if download(video["baseUrl"]):
            #     break
        mp4_url = jsons["data"]["dash"]["video"][0]["baseUrl"]

    data = jsons["data"]
    return


def download_mp3_mp4(mp3url, mp4url, filename):
    # 检查视频大小
    headers = {
        'Range': 'bytes={}-{}'.format(0, 100),
        'Referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    resp = requests.get(mp4url, headers=headers)
    if int(resp.headers.get('content-range').split('/')[-1]) < value.max_video_length * 1048576:
        # print(resp.headers.get('content-range').split('/')[-1])
        # download_mp4_mp3.download_mp3_mp4(mp3url, mp4url, filename)
        return 0


def main():
    download_video('')
    return


if __name__ == '__main__':
    main()
