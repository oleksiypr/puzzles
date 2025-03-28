import numpy as np


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


def length(keys_path):
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


assert length([])        == 0.
assert length([A, A])    == 0.
assert length([A, E])    == dist(A, E)
assert length([E, A])    == dist(A, E)
assert length([E, A, T]) == length_EAT
assert length([A, T, E]) == length_ATE