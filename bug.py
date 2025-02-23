def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    return x / y