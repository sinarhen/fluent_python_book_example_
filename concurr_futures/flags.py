import sys
import time

import requests

POP20_CC = 'CN IN US ID PK BR NG BD RU MX JP PH EG DE IR TR CD FR'.split()

DEST_DIR = 'downloads/'


def get_flag(cc):
    url = f"https://www.worldatlas.com/r/w425/img/flag/{cc.lower()}-flag.jpg"
    resp = requests.get(url)
    return resp.content


def save_flag(img, filename):
    with open(f'{DEST_DIR}{filename}.jpg', 'wb') as fp:
        fp.write(img)


def download_flag(cc_list):
    for cc in cc_list:
        image = get_flag(cc)
        print_downloads(cc)
        save_flag(image, cc.lower())
    return len(cc_list)


def print_downloads(text):
    print(f'{text} downloaded 100%')
    sys.stdout.flush()


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print(f'\n {count} flags downloaded in {elapsed} seconds')


if __name__ == '__main__':
    main(download_flag)
