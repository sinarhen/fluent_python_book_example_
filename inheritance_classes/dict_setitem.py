class DoppelDict(dict):

    def __setitem__(self, key, value):
        super(DoppelDict, self).__setitem__(key, [value]*2)


dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)
"""RESULT
{'one': 1}
{'one': 1, 'two': [2, 2]}
{'one': 1, 'two': [2, 2], 'three': 3}
"""


from collections import UserDict


class Custom(UserDict):
    def __setitem__(self, key, value):
        super(Custom, self).__setitem__(key, [value]*2)


dd = Custom(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)

"""RESULT
{'one': [1, 1]}
{'one': [1, 1], 'two': [2, 2]}
{'one': [1, 1], 'two': [2, 2], 'three': [3, 3]}
"""
"""
Conclusion
For builtins classes use collections.User...
"""