# Uncommon Python Error: Unhandled ZeroDivisionError

This repository demonstrates a subtle bug involving an unhandled `ZeroDivisionError` in Python. The error only occurs when a specific condition is met, making it less obvious during initial testing.

## Bug Description
The `function_with_uncommon_error` function divides `x` by `y`.  However, it doesn't explicitly check for the case where `x` is 0 before the division, leading to a `ZeroDivisionError` when `x` is 0.  This is a common type of error and easily overlooked if the condition is complex or rarely encountered.

## Solution
The solution involves adding a check to handle the case where `x` is 0, preventing the `ZeroDivisionError`.

## How to Reproduce
1. Clone the repository.
2. Run `bug.py`. You'll get a `ZeroDivisionError`.
3. Now run `bugSolution.py` to see the fixed version.
