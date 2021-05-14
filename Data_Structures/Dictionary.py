class Dictionary():
    def demo_syntax(self):
        """
        Demmo syntax of Dictionary

        """
        d1 = {"a": 1, "b": 2, "c": 3}
        d2 = {"a": {1: "x", 2: "y"}, "b": 2, "c": 3}
        d3 = {x: x * 2 for x in range(5)}

        print(d1["a"])  # 1
        print(d2["a"][1])  # x
        print(d3)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
        print(d1.keys())  # dict_keys(['a', 'b', 'c'])
        print(d1.values())  # dict_values([1, 2, 3])
        d1.update(d3)
        print(d1)  # {'a': 1, 'b': 2, 'c': 3, 0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

    def example(self):
        """
        create dict from zip and sum it

        """

        dic = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
        sum = 0
        for d in dic.keys():
            sum += dic[d]
        print(f"value of dictionary sum ={sum}")


Dictionary().demo_syntax()
Dictionary().example()
