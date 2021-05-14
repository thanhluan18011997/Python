def test(*args) -> int:
    """
       learn function

       """
    s = 0
    for i in args:
        s = s * int(i)
    return s


args = [1, 2, 3, 4]
test(*args)


def test_function(s=1, *args, **kwargs):
    """
    unpack in python

    """
    s = 0
    for i in args:
        s = s + int(i)
    print(s)

    for k, v in kwargs.items():
        print("with key={key} match value={value}".format(key=k, value=v))


test_function(1, 2, 3, name="luan", year=24)


def test_param(*args, x):
    """
    test param *args
    :param args:
    :param x:
    :return:
    """
    if len(args) > 0:
        for i in args: print("=>", i + x)


test_param(1, 2, 3, x=10)


def test_lambda():
    """
       learn lambda

       """
    # tim ucln viet bang lambda
    ucln = lambda a, b: a if a == b else ucln(a - b, b) if a > b else ucln(a, b - a)
    print(ucln(4, 20))

    # tinh giai thua bang lambda
    gt = lambda n: 1 if n < 2 and n >= 0 else gt(n - 1) * n
    print(gt(0))

    def check_prime(n=2):
        """
        check n is prime?
        :param n:
        :return:true or false
        """
        if n == 2:
            return True
        elif n < 2:
            return False
        else:
            for i in range(2, n):
                if n % i == 0: return False
            return True

    nguyen_to = list(map(lambda x: x * 2, list(filter(check_prime, range(10)))))
    print(nguyen_to)


test_lambda()
