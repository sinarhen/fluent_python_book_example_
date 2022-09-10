import time


def clock(func, *args, **kwargs):
    t0 = time.time()
    f = func(*args, **kwargs)
    t = time.time() - t0
    return t

