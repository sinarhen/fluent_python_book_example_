from concurrent import futures

from flags import *

DEST_DIR = 'download_flags_futures/downloads_futures/'


def download_one(cc):
    img = get_flag(cc)
    print_downloads(cc)
    save_flag(img, cc.lower())
    return cc


def download_many_flags(cc_list):
    with futures.ThreadPoolExecutor(max_workers=20) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


if __name__ == '__main__':
    main(download_many_flags)
