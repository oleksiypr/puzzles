import numpy as np

cos_a = 1/np.sqrt(5)


def dist(K1, K2):
    """
    Compute distance between two keys on a keyboard.
    :param K1: coordinates of key 1 as a tuple (x1, y1)
    :param K2: coordinates of key 2 as a tuple (x2, y2)
    :return: distance
    """
    x1, y1 = K1
    x2, y2 = K2

    dx = x2 - x1
    dy = y2 - y1
    return np.sqrt(dx**2 + dy**2 - 2*dx*dy*cos_a)

assert dist((2, 2), (2, 2)) == 0.
assert dist((0, 0), (0, 0)) == 0.
assert dist((0, 1), (2, 2)) == dist((2, 2), (0, 1))
assert dist((1, 1), (2, 3)) == dist((2, 3), (1, 1))

A = 0, 1
E = 2, 2
T = 4, 2

s_EAT = dist(E, A) + dist(A, T)
s_ATE = dist(A, T) + dist(T, E)

print(f"EAT: {s_EAT:<3.3f}")
print(f"ATE: {s_ATE:<3.3f}")

if s_EAT < s_ATE:
    print("=> EAT more probable then ATE")
elif s_EAT > s_ATE:
    print("=> ATE more probable then EAT")
else:
    print("=> ATE is as probable as EAT")


