import json
import os
import requests


def main():
    upload_url = ''
    for f in os.listdir('f'):
        if f.find('.json') > 0:
            jso = json.load(open('f/{}'.format(f), 'r', encoding='utf-8'))
            # print(jso)
            import subprocess
            subprocess.call('curl' )


if __name__ == '__main__':
    main()
