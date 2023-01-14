"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

class cons:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def car(self):
        return self.a

    def cdr(self):
        return self.b

if __name__ == "__main__":
    c = cons(3,4)
    print(c.car())
    print(c.cdr())