def mult(m, n):
    try:
        return m * n

    except TypeError as TE:
        return TE.__str__()

    except ArithmeticError as AE:
        return AE.__str__()


def curry(func, var):
    return lambda x: func(var, x)


mult_curry_prev = lambda m: curry(mult, m)

mult_curry = lambda n: mult_curry_prev(n)
