def statement_if():
    s = 1
    k = 0
    if s == 1:
        k = 1
    elif s == 2:
        k = 2
    else:
        k = 3

    assert k == 1


def statement_for():
    """for/in/break/continue/else"""
    lst = [-1, 0, 1, 2, 3, 4, 25, 37]
    k = 0
    p = 0
    for i in lst:
        if i > 10:
            break
        if i < 0:
            continue
            k += i
    else:  # execute this part if no break happened
        p = 1
    assert k == 10
    assert p == 0


if __name__ == '__main__':
    statement_if()
