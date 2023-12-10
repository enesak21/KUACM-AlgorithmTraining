def fastPow(n, p):
    print("here")
    if p == 0:
        return 1

    res = fastPow(n, p // 2)
    if p % 2 != 0:
        return res * res * n
    return res * res
