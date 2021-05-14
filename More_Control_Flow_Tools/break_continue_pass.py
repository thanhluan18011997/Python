def test_break_continue_pass():
    """
      Learn break, continue and pass

      """

    for i in range(10):
        if i == 5:
            continue
        elif i == 7:
            pass
        elif i == 9:
            break
        print(f"number {i}")


test_break_continue_pass()
