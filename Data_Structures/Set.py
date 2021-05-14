def demo_set():
    """
    demo set
    :return:
    """
    s = {"luan", "dz", "qua", "di", "luan", "dz"}
    print(s)
    dic = {1: "a", 2: "b", 3: "c"}
    l = set(dic.keys())
    print(l)
    s1 = {x // 2 for x in range(10, 20) if x % 2 == 1}
    print(s1)


demo_set()
