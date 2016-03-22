#!/usr/bin/env python3


def sum_div(n):
    """Return a list of elements that takes its sum leads to the given n
       parameter.

    Example: n=6 returns  [1, 2, 3]
             n=5 returns  [1, 4]
             n=10 returns [1, 2, 3, 4]

    """
    if n == 1:
        return [1]

    l = []
    curr_rem = n
    for i in range(1, n):
        if curr_rem - i >= 0:
            l.append(i)
            curr_rem -= i
            if curr_rem == 0:
                break
        else:
            # Backtracking
            last_sum = l.pop()
            curr_rem += last_sum
    return l
