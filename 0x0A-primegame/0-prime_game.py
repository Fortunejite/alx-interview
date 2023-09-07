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
    """
    Determine the winner of multiple rounds of the game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing n for each round.

    Returns:
        str or None: The name of the player with the most wins (Maria or Ben), or None if it's a tie.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

