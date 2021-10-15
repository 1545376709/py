import os
import ssl
import requests
import certifi
import urllib3

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

env_list = os.environ
ssl._create_default_https_context = ssl._create_unverified_context
print(certifi.where())
urllib3.disable_warnings()
headers = {
    'Range': 'bytes={}-{}'.format(0, 100),
    'Referer': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
                  'Safari/537.36 '
}
mp4url = 'https://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/17/60/362336017/362336017_nb2-1-30280.m4s?e' \
         '=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1634266574&gen=playurlv2&os=kodobv&oi=3395606116&trid=6cdac482c6e246a3b1ee81c11fbdb38eu&platform=pc&upsig=419f0a4584a9b1db989a07871eb594c4&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=361401613&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000 '
resp = requests.get(mp4url, headers=headers,verify=False)
print(resp.text)
print(env_list.get('SSL_CERT_DIR'))
print(env_list.get('SSL_CERT_FILE'))
print(env_list.get('LDFLAGS'))
print(env_list.get('CPPFLAGS'))
print(env_list.get('PKG_CONFIG_PATH'))
print(env_list.get('PATH'))

print("all evn list:")

# print all
for key in env_list:
    print(key + ' : ' + env_list[key])
