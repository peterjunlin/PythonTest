"""
random.randint(1, 6)
"""

import random


def random_when_repeat():
    """how long the random sequence can repeat a number in a row."""
    num_cases = 100
    num_repeated = 6

    average_i_repeated = 0
    for i in range(num_cases):
        count_repeated = 0
        t0 = -1
        i_when_repeated = 0
        while count_repeated < num_repeated:
            i_when_repeated += 1
            t = random.randint(0, 10)
            # print(i_when_repeated, t)
            if t == t0:
                count_repeated += 1
            else:
                count_repeated = 0
                t0 = t

        print(i_when_repeated)
        average_i_repeated += i_when_repeated

    print("Average = ", average_i_repeated / num_cases)


if __name__ == '__main__':
    random_when_repeat()
