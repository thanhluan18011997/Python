def demo_tuple():
    """
    learn tuple...
    """
    t = 1, 2, "luan", [4, 5, 6]
    print(t)
    print(t[0], t[3][1])
    t2 = tuple([1, 5, 6])
    t3 = t, t2
    print(t3)
    t3 = t + t2
    print(t3)
    t4 = tuple(zip((1, 2, 3), ["a", "b", "c"]))
    print(t4)

    t5 = (x ** 2 for x in t2)
    for i in t5: print(i)

    print((1, 2) < (1, 2, -1))


demo_tuple()
