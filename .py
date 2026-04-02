def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

single_step = lambda x, n: (x**n) / factorial(n)

def exp_x(x, n):
    total = 0
    for i in range(n):
        total += single_step(x, i)
    return total

global_sum = 0

def solve_sn(n):
    """
    Calculates the alternating harmonic series Sn recursively.
    The sign is determined by whether n is odd or even: 
    (-1)^(n+1) is 1 for odd n and -1 for even n.
    The function updates the global_sum and returns nothing.
    """
    global global_sum
    if n == 0:
        return
    
    solve_sn(n - 1)
    
    term = 1 / n
    if n % 2 == 0:
        global_sum -= term
    else:
        global_sum += term

