#!/usr/bin/python3
def is_prime(n):
    """
    Check if a number n is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def play_round(n):
    """
    Simulate a single round of the game for a given n.

    Args:
        n (int): The number for the current round.

    Returns:
        str: The name of the winner (Maria or Ben).
    """
    maria_turn = True
    while n > 1:
        prime_found = False
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                n -= i
                prime_found = True
                break
        if not prime_found:
            break
        maria_turn = not maria_turn
    return "Maria" if maria_turn else "Ben"


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
