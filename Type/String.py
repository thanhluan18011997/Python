def syntax_String():
    """
      Learn String type

      """
    s1 = "thanh luan"
    s2 = "nguyen" + " " + s1
    print(s2)
    l = s2.split()
    print(l)
    s3 = s2.replace("n", "xxx")
    print(s3)
    print(s2)
    print(s2.find("ng"))
    print(s2.upper())
    print(s2.lower())
    l1 = list(s2)
    print(l1)
    print(r"c:/user/doc")
    print(len(s2))
    print(s2[:2])
    s2 = "     " + s2 + "       "
    s2.strip()
    print("luan" in s2)


syntax_String()
