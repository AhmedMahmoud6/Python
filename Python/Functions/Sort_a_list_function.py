def test(numbers, order):
    if order == 'none':
        return numbers

    elif order == 'asc':
        x = sorted(numbers, reverse=False)
        return x

    elif order == 'desc':
        y = sorted(numbers, reverse=True)
        return y
    return
