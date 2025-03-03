import numpy as np
import matplotlib.pyplot as plt


p = .80 # probability of 1 USD prize per attempt
q = .15 # probability of 3 USD prize per attempt
g = .05 # probability of 10 USD prize per attempt

assert p + q + g == 1.0

# Part 1
n = 8 # attempts

"""
Probability that attempt will not result to 10 USD prize
"""
a = 1 - g
assert np.isclose(a, p + q)


def threshold(p):
    """
    Minimum remaining attempts at which the probability that the player
    wins is not less than 3 USD more than vice versa.
    :param p: probability to win less than 3 USD per attempt
    :return: minimum remaining attempts
    """
    return np.ceil(-np.log(2)/np.log(p))


t0 = threshold(p)
assert np.isclose(threshold(0.8), 4.0)


def prise_p(n, t):
    """
    Probability that the player takes 1 USD prize for the game.
    :param n: attempts
    :param t: threshold
    :return: probability
    """
    return a**(n - t) * p**t

def prise_q(n, t):
    """
    Probability that the player takes 3 USD prize for the game.
    :param n: attempts
    :param t: threshold
    :return: probability
    """
    res = q*(1 - p**t)
    res = res/(1 - p)
    res = res * a**(n -t)
    return res


def prise_g(n, t):
    """
    Probability that the player takes 10 USD prize for the game.
    :param n: attempts
    :param t: threshold
    :return: probability
    """
    res = g*(1 - p**t)
    res = 1 - res/(1 - p)
    res = 1 - res*a**(n - t)
    return res


def expected_prize_1(n):
    if n < t0:
        t1 = n
    else:
        t1 = t0

    P1__1_USD = prise_p(n, t1)
    P1__3_USD = prise_q(n, t1)
    P1_10_USD = prise_g(n, t1)
    assert np.isclose(P1__1_USD + P1__3_USD + P1_10_USD, 1.0)
    return P1__1_USD*1.0 + P1__3_USD*3.0 + P1_10_USD*10.0


assert np.isclose(expected_prize_1(1), 1.*p + 3.*q + 10*g)


# Part 2: 2 prizes and 10 attempts
m = 10    # part-2 game attempts
k = m - 1 # maximum attempts to take the 1st prize

"""
Expectation of the prize when the 1st prize was 1 USD 
"""


def expected_prize_2(t):
    """
    :param t: current threshold
    :return:
    """
    assert k > t
    m_p = a**(k-t) * p**t * expected_prize_1(1)

    def m_q():
        res = 3.0*(1-p**t)/(1-p)
        res = res + sum([p**i * expected_prize_1(t-i) for i in np.arange(0, t)])
        res = res * a**(k-t) * q
        return res

    def m_g():
        res = a**(k-t)*g*(1-p**t)/(1-p)
        res = res + 1 - a**(k-t)
        res = 10.0*res
        res = res + g*sum([a**i * expected_prize_1(k-i) for i in np.arange(0, t+1)])
        res = res + a**(k-t)*g*(
            sum([p**i * expected_prize_1(t-i) for i in np.arange(0, t)])
        )
        return res

    return m_p + m_q() + m_g()

'''
print(f'Expected optimal prize prise in game#2 for threshold {t0}: {expected_prize_2(t0):.3f} USD')

t_values = np.arange(0, k)
expected_values = [expected_prize_2(t) for t in t_values]

plt.scatter(t_values, expected_values, color='blue', label='Expected Prize, USD')
plt.xlabel('n')
plt.ylabel('Expected Prize in Game 2')
plt.ylim(0)
plt.title('Expected Prize vs. threshold')
plt.legend()
plt.grid()
plt.show()
'''











