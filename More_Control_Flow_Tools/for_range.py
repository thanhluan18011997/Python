def test_for_range():
    """
      Learn for and range

      """
    while True:
        n = int(input("Please input n= "))
        if n > 0: break

    for i in range(n):
        print(i ** 2)
    else:
        print("end!!")

    for i in "nguyen thanh luan":
        print(i.upper())


test_for_range()
