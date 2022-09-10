import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # 3
        status = f'{char} {msg}'
        write(status)
        flush()
        write('\x08' * len(status))  # 4
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42


@asyncio.coroutine
def supervisor():
    spinner = asyncio.ensure_future(spin('thinking'))


