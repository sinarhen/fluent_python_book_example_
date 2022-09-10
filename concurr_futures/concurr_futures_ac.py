from concurrent import futures

from flags import *

DEST_DIR = 'downloads/'


def download_one(cc):
    img = get_flag(cc)
    print_downloads(cc)
    save_flag(img, cc.lower())
    return cc


def download_many_flags(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print(f'{future} result: {res}')
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many_flags)
