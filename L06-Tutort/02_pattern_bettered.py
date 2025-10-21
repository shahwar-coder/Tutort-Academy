'''
n=5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

def helper_func(n: int, i: int) -> None:
    """Print one line of a hollow diamond for half-size n at row i (1-based)."""
    left_spaces = " " * (n - i)
    middle_spaces = " " * (2 * (i - 1))
    if i == 1:
        print(left_spaces + "*")
    else:
        print(left_spaces + "*" + middle_spaces + "*")


def print_hollow_diamond(n: int) -> None:
    """Print a hollow diamond of size n (upper half has n rows)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    for i in range(1, n + 1):
        helper_func(n, i)
    for i in range(n - 1, 0, -1):
        helper_func(n, i)


# usage
print_hollow_diamond(5)

    
