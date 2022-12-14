import collections


class Dict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


d = {'Молоток': 1, "Перчатки(пар)": 2, "Лопата": 3}
d1 = Dict(d)

print('Молот' in d1)
