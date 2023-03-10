#!/usr/bin/python3

"""
Prime Game

Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

Args:
    x(int): number of rounds
    n(list): list of numbers

Returns:
    "Maria" if no prime number for Ben
    "Ben" if no prime number for Maria
    "None" if no winner
"""


def isWinner1(x, nums):
    if not nums or x < 1:
        return None
    n = max(nums)
    K = [b for b in range(max(n + 1, 2))]
    for i in range(2, int(n**0.5) + 1):
        if not K[i]:
            continue
        for j in range(i*i, n + 1, i):
            K[j] = False

    K[0] = K[1] = False
    c = 0
    for i in range(len(K)):
        if K[i]:
            c += 1
        K[i] = c

    players = {"maria": 0, "ben": 0}
    for n in nums:
        players["maria"] += K[n] % 2 == 1

    if players["maria"] * 2 == len(nums):
        return None
    if players["maria"] * 2 > len(nums):
        return "Maria"
    return "Ben"
