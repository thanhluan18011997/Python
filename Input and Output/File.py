def workWithFile():
    """
    learn read, write file
    :return:
    """
    with open(r"./luan.txt","w") as f:
        f.write("hello luan \n Do you ready lear django?")

    with open(r"./luan.txt","r") as f:
        src=f.read()
        print(src)
        s=""
        for x in f:
            s+=x
        print(s)

    with open(r"./luan.txt","r") as f:
        print("Read per line and line:\n")
        s=""
        for x in f:
            s+=x
        print(s)


workWithFile()