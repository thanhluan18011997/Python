def learnPrintFunction():
    """
    learn print() and string format
    :return:
    """
    name = input("please input your name:")
    print("hello ", name)

    while True:
        years = int(input("how old are you, {} \n".format(name)))
        if int(years) == years: break
    print(f"{name} is handsome :))")


learnPrintFunction()
