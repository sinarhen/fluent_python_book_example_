class Foo:

    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
print(f[1])
for i in f:
    print(i)
    
