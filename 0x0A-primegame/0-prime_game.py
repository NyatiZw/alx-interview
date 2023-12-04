#!/usr/bin/python3
""" function to find the prime number """


def isWinner(x, nums):
    """Function to determine winner"""
    def is_prime(num):
        """Helper function to determine if num is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """Helper function to get primes"""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def game_winner(n):
        """Helper function to determine game winner"""
        primes = get_primes(n)
        total_moves = len(primes)
        if total_moves % 2 == 1:
            return "Maria"
        else:
            return "Ben"

    wins = {"Maria": 0, "Ben": 0}

    for i in range(x):
        winner = game_winner(nums[i])
        wins[winner] += 1

    max_wins = max(wins.values())
    if list(wins.values()).count(max_wins) == 1:
        return max(wins, key=wins.get)
    else:
        return None
