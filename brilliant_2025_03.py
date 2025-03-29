import numpy as np

"""
Bored at work, you start typing random keys on your keyboard. 
Are you more likely to type EAT or ATE first?

Bonus: The random typing continues. 
What is the probability that you type TALES before STALE?
"""


# Solution

"""
If the total distance traveled by a user's finger is shorter for one sequence 
than another, then that sequence is more likely to be typed.

For example:
 - EA is distance between keys `E` and `A` on a keyboard, the same for AT and TE.
 - If EA + AT < AT + TE, then it is more likely that the user will type "EAT".
 - If EA + AT > AT + TE, then it is more likely that the user will type "ATE."
 - Otherwise, "ATE" and "EAT" are equally likely to be typed.

Assume all keyboard keys are square-shaped, with dimensions of 1 unit by 1 unit.
Each key in the layer below is positioned exactly in the middle of two keys in the layer above.
Thus, we can model the keyboard as a parallelogram grid with angles `a` and `180° - a`.
The coordinate of a key is defined as the coordinate of the lower-left corner of its cell in the grid.
"""

cos_a = 1/np.sqrt(5)


def dist(k1, k2):
    """
    Compute distance between two keys on a keyboard.
    :param k1: coordinates of key 1 as a tuple (x1, y1)
    :param k2: coordinates of key 2 as a tuple (x2, y2)
    :return: distance
    """
    x1, y1 = k1
    x2, y2 = k2

    dx = x2 - x1
    dy = y2 - y1
    return np.sqrt(dx**2 + dy**2 - 2*dx*dy*cos_a)


assert dist((2, 2), (2, 2)) == 0.
assert dist((0, 0), (0, 0)) == 0.
assert dist((0, 1), (2, 2)) == dist((2, 2), (0, 1))
assert dist((1, 1), (2, 3)) == dist((2, 3), (1, 1))


A = 0, 1
E = 2, 2
L = 8, 1
S = 1, 1
T = 4, 2


length_EAT = dist(E, A) + dist(A, T)
length_ATE = dist(A, T) + dist(T, E)
print(f"EAT: {length_EAT:<3.3f}")
print(f"ATE: {length_ATE:<3.3f}")


if length_EAT < length_ATE:
    print("=> EAT more probable then ATE")
elif length_EAT > length_ATE:
    print("=> ATE more probable then EAT")
else:
    print("=> ATE is as probable as EAT")


def dist_sum(keys_path):
    """
    Computes length of keys path as a sum of edges:
    length([A, T, E, B]) -> AT + TE + EB
    :param keys_path: list of key coordinates, ex.: [(0, 0), (0, 1), (2, 2)]
    :return: length of the path
    """
    hi = keys_path[:-1]
    lo = keys_path[1:]

    keys_tuples = list(zip(hi, lo))
    lengths     = [dist(kk[0],kk[1]) for kk in keys_tuples]
    return sum(lengths)


assert dist_sum([]) == 0.
assert dist_sum([A, A]) == 0.
assert dist_sum([A, E]) == dist(A, E)
assert dist_sum([E, A]) == dist(A, E)
assert dist_sum([E, A, T]) == length_EAT
assert dist_sum([A, T, E]) == length_ATE


# Bonus
"""
We know that the user typed either `TALES` or `STALES`. Typing `TALES` before 
`STALES` means:
1. The letter `S` was typed after typing `TALE`.
2. Conversely, typing `STALES` before `TALES` means the letter `S` was typed before `TALE`. 

Effectively, this means that the probability of typing "TALES" before "STALES" 
is the same as the probability of condition 1 occurring.
"""
len_TALE  = dist_sum([T, A, L, E])
len_ES    = dist_sum([E, S])
len_ST    = dist_sum([S, T])
len_TALES = len_TALE + len_ES
len_STALE = len_ST   + len_TALE


P_TALES = len_TALES / (len_TALES + len_STALE)
P_STALE = len_STALE / (len_TALES + len_STALE)
print("\n")
print(f"The probability that you type TALES before STALE: {P_TALES:<1.2f}")
print(f"The probability that you type STALE before TALES: {P_STALE:<1.2f}")
