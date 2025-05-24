def powers_of_three(limit=None):
    exponent = 0
    while limit is None or exponent <= limit:
        yield 3 ** exponent
        exponent += 1