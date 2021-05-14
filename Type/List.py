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
