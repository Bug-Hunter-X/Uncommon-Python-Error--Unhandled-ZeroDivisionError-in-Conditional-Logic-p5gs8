def function_with_uncommon_error(x, y):
    if x == 0:
        return float('inf') # Handle division by zero appropriately.  Could also raise an exception or return a specific value
    return x / y