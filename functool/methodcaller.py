from operator import methodcaller

int_nums = methodcaller('replace', ' ', '',)
strng = 'Omg im done'
print(int_nums(strng))
