registry = set()


def register(active: bool = True):
    def decorate(func):
        print(f'running register(active: bool={active})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate


@register(active=True)
def f1():
    print('running f1()')


@register(active=False)
def f2():
    print('running f2()')


def f3():
    print('running f3()')
