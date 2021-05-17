from urllib.parse import ParseResult


class List:

    def demo_syntax(self):
        """
        Demmo syntax of List

        """
        l1 = [1, 2, 3, 4, 5]
        l2 = list("ThanhLuan")
        l3 = list(range(-4, 4))
        l4 = [2, "luan", {"a": 1, "b": 2}, (1, 2)]
        l5 = [x ** 2 for x in range(1, 5)]

        print(l1.pop(2))  # 3
        print(l2[5:])  # ['L', 'u', 'a', 'n']
        l1.extend(l2)
        print(l1)  # [1, 2, 4, 5, 'T', 'h', 'a', 'n', 'h', 'L', 'u', 'a', 'n']
        print(l4[1][0])  # l
        print(l5[::-1])  # [16, 9, 4, 1]
        print(len(l2))  # 9
        l2.insert(len(l2), "DZ")
        print(l2)  # ['T', 'h', 'a', 'n', 'h', 'L', 'u', 'a', 'n', 'DZ']
        l3.reverse()
        print(l3)  # [3, 2, 1, 0, -1, -2, -3, -4]
        l3.remove(0)
        print(l3)  # [3, 2, 1, -1, -2, -3, -4]

    def example(self):
        """
        generate fibonanci with list

        """
        fibo = [1]
        a, b = 1, 2
        n = 10
        for i in range(n):
            fibo.append(b)
            a, b = b, a + b
        print(fibo)  # [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]


List().demo_syntax()
List().example()


class Stack:
    """
    using list same a stack
    """

    def __init__(self, list: list):
        self.list = list

    def pop(self):
        return self.list.pop()

    def push(self, x):
        self.list.append(x)


stack = Stack([1, 2, 3])
print(stack.pop())  # 3
stack.push(5)
print(stack.list)  # [1, 2, 5]

"""
using list same queue

"""
from collections import deque

deque = deque([1, 2, 3, 4])
deque.append(5)
print(deque)  # deque([1, 2, 3, 4, 5])
print(deque.popleft())  # 1

"""
list comprehension
"""

l1 = [x ** x for x in range(5) if x % 2 == 0]
print(l1)  # [1, 4, 256]
q = lambda x, a=10: x * a
l2 = [q(x) for x in range(5) if x % 2 == 0]

print(l2)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = [x for i in matrix for x in i]
print(l)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
z = dict(zip([1, 2, 3], [4, 5, 6]))
print(z)

del l[0]
print(l)  # [2, 3, 4, 5, 6, 7, 8, 9]

# region Description
l2 = sorted(l, reverse=True)
print(l2)
# endregion
print()
with open("NameTuple.py") as f:
    src=f.read()
    print(src)
    print(f.__dict__)

