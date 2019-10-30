def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)    # print(do_it(5))

def do_something(n):
    """Print the positive numbers in squares from n down to 0."""
    # if result is zero, loop is complete, just return
    if n < 0:
        return
    # no else statement is needed, if we have not hit the base case
    # print the square of n, repeat the process with n - 1
    print(n ** 2)
    do_something(n - 1)

do_something(4)

def calculate_blocks(rows):
    """Calculate blocks needed for a given number of rows of a 2D pyramid."""
    # base case: zero blocks are needed for zero or less rows
    if rows <= 0:
        return 0
    # recursive case: each row includes same number of blocks as its row number, including the rest of it
    return rows + calculate_blocks(rows -1)

def build_pyramid():
    """Get user's pyramid size in rows and output the blocks needed."""
    # chosen_rows = 6
    chosen_rows = int(input("How many rows is your pyramid: "))
    print("For {} rows, you need {} blocks".format(chosen_rows, calculate_blocks(chosen_rows)))

build_pyramid()