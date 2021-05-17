def learnException():
    """
    learn exception
    :return:
    """
    try:
        a=1/0
    except ZeroDivisionError:
        print("divide zero... ")

    while True:
        try:
            a= int(input("Please input a number\n"))
            break
        except Exception:
            print("Not nummber, try again!!")
        finally:
            print(":))))))")


    class LuanException(Exception):
        def __init__(self,message):
            self.message=message

    try:
        raise LuanException("Luan is handsome")
    except LuanException:
        print("Exactly!!!")


learnException()
