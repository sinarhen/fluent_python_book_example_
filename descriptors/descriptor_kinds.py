def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split()


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif isinstance(int | type(None), cls):
        return repr(obj)
    return f'{cls_name(obj)} object'


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}__{name}__({pseudo_args})')


class Overriding:

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding

    def spam(self):
        print(f'-> Managed spam({display(self)})')
