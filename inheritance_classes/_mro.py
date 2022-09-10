class A:
    def ping(self):
        print('ping:', self)


class B(A):

    def pong(self):
        print('Pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
