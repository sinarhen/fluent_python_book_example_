import sys


class LookingGlass:

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        return self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('НЕ надо делить на ноль')
            return True


with LookingGlass() as mr:
    print('Alice in the')
    print(mr)
