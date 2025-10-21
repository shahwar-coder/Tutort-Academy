def print_hollow_line(n: int, i: int) -> None:
    """
    Print one line of the hollow diamond pattern.
    
    Parameters:
    n (int): Total number of rows in one half of the diamond.
    i (int): Current row index (1-based).
    """
    left_spaces = " " * (n - i)
    middle_spaces = " " * (2 * (i - 1))
    if i == 1:
        print(left_spaces + "*")
    else:
        print(left_spaces + "*" + middle_spaces + "*")


def print_hollow_diamond(n: int) -> None:
    """
    Print a hollow diamond pattern made of '*' for a given size n.

    Example for n = 5:
        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *
    """
    # Upper half (including the middle line)
    for i in range(1, n + 1):
        print_hollow_line(n, i)

    # Lower half
    for i in range(n - 1, 0, -1):
        print_hollow_line(n, i)
