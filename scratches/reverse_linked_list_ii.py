def cons(a, b):
    return a, b


def car(xs):
    return xs[0]


def cdr(xs):
    return xs[1]


def create(*xs):
    if len(xs) == 1:
        return cons(
            car(xs),
            None,
        )
    else:
        return cons(
            car(xs),
            create(*xs[1:]),
        )


def reverse(xs):
    ...


if __name__ == '__main__':
    print(
        create(1, 2, 3, 4, 5)
    )
    print(
        create(5, 4, 3, 2, 1)
    )
