class O:
    def method(self):
        print('I am O')

class A(O):
    def method(self):
        super().method()
        print('I am A')

class B(O):
    def method(self):
        super().method()
        print('I am B')


class C(A, B):
    def method(self):
        super().method()
        print('I am C')

if __name__ == "__main__":
    C().method()