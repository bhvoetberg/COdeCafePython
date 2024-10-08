import random
import time


def flag_sort(flag):
    i: int = 0
    j: int = 1
    k: int = len(flag) - 1

    while j < k:
        if flag[i] == 2:
            flag[i], flag[k] = flag[k], flag[i]
            k -= 1
        if flag[i] == 1 and j < k:
            flag[i], flag[j] = flag[j], flag[i]
            j += 1
        if flag[i] == 0:
            i += 1
            # j += 1
    return flag


def main():
    flag: list[int] = [1, 0, 2, 0, 0, 0, 0, 2, 2, 1, 2, 0, 1, 1, 1, 0, 2, 0, 0, 0, 2, 1, 1, 1, 2, 2, 0, 2, 2, 1, 2, 1,
                       0, 1, 1, 1, 1, 2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 1, 2, 2, 0, 2, 2, 0, 0, 2, 1, 2, 1, 1, 2, 2, 2,
                       0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 2, 2, 1, 0, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 0, 1, 1,
                       0, 1, 0, 2, 0, 0, 2, 2, 1, 0, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 2, 1, 0, 2, 0, 1, 2, 1, 1, 1, 2, 2,
                       0, 0, 2, 1, 0, 2, 2, 0, 1, 0, 0, 1, 0, 2, 1, 1, 1, 2, 2, 1, 0, 2, 0, 1, 2, 0, 2, 0, 2, 2, 1, 0,
                       1, 2, 2, 2, 1, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 1, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2,
                       1, 1, 0, 2, 0, 2, 2, 1, 1, 2, 1, 1, 2, 1, 0, 2, 1, 1, 1, 2, 1, 2, 2, 1, 2, 0, 2, 1, 2, 2, 1, 2,
                       1, 1, 2, 1, 1, 1, 0, 2, 2, 1, 1, 0, 1, 1, 0, 0, 1, 2, 1, 2, 2, 0, 1, 2, 1, 1, 1, 0, 2, 1, 1, 1,
                       1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 1, 0,
                       0, 2, 1, 2, 2, 0, 1, 1, 2, 1, 1, 0, 2, 2, 2, 2, 1, 2, 0, 0, 0, 1, 1, 0, 2, 0, 1, 1, 1, 1, 0, 2,
                       0, 0, 1, 2, 0, 0, 0, 1, 0, 1, 1, 2, 0, 2, 2, 2, 0, 0, 1, 2, 1, 0, 1, 2, 0, 2, 1, 1, 1, 0, 2, 0,
                       0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 1, 2, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 2, 2, 2, 0, 2, 0, 2, 2, 0, 1,
                       2, 1, 2, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 2, 0, 2, 1, 2, 0, 0, 0, 1, 1, 2, 0, 1, 0,
                       0, 0, 2, 2, 2, 2, 0, 1, 2, 0, 2, 2, 1, 1, 2, 1, 1, 0, 0, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1,
                       1, 0, 2, 2, 0, 1, 2, 1, 2, 0, 2, 0, 2, 2, 0, 1, 0, 2, 0, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 2, 2, 1,
                       0, 1, 2, 1, 1, 1, 2, 0, 1, 2, 2, 0, 2, 1, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 2, 2, 0, 1, 0, 0, 1, 1,
                       2, 1, 2, 2, 1, 0, 2, 1, 2, 2, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2, 1, 0, 2, 2, 2, 0, 0, 1, 0,
                       2, 2, 2, 1, 2, 0, 2, 0, 1, 0, 0, 2, 2, 2, 2, 1, 0, 0, 1, 0, 2, 1, 2, 0, 1, 1, 1, 0, 2, 2, 1, 1,
                       1, 2, 1, 2, 1, 2, 0, 0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 2, 1, 2,
                       1, 2, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 0, 2, 2, 1, 0, 1, 2, 1, 1, 0, 2, 2, 0, 1, 0,
                       1, 2, 2, 0, 1, 2, 1, 2, 1, 2, 1, 2, 0, 2, 2, 0, 1, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 2, 1, 1, 2, 1,
                       0, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 2, 0, 2, 1, 0, 1, 0, 0, 1, 1, 2, 2, 1, 0, 2, 2, 2, 2, 0, 2,
                       0, 2, 0, 1, 1, 0, 2, 2, 2, 0, 1, 0, 1, 1, 2, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1, 2, 1, 0, 2, 2, 2,
                       0, 1, 1, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0, 1, 2, 0, 1, 2, 2, 0, 2, 0, 1, 1, 0, 0, 2, 0, 1, 1, 1, 1,
                       0, 2, 2, 0, 2, 2, 0, 1, 2, 1, 2, 0, 0, 2, 2, 0, 1, 1, 0, 1, 0, 0, 0, 2, 2, 0, 1, 0, 1, 2, 2, 0,
                       2, 2, 2, 2, 0, 0, 2, 2, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 2, 1, 0, 1, 2, 0, 1, 0, 2, 0, 0,
                       2, 0, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2, 1, 1, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0,
                       2, 1, 1, 0, 2, 0, 2, 2, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 2, 2, 1, 0, 1, 2, 1, 1, 1, 2, 1, 2, 0, 1,
                       1, 0, 2, 1, 2, 2, 0, 2, 1, 2, 2, 0, 2, 1, 2, 1, 2, 0, 2, 1, 1, 2, 0, 1, 2, 0, 0, 1, 2, 2, 0, 2,
                       2, 1, 0, 1, 1, 2, 1, 2, 2, 0, 2, 1, 2, 2, 1, 0, 1, 0, 1, 2, 1, 1, 2, 1, 0, 0, 2, 0, 0, 2, 2, 2,
                       2, 0, 2, 0, 2, 0, 1, 1, 1, 1, 2, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 1, 2, 1, 1, 2, 0, 1, 2, 0, 1, 1,
                       2, 1, 1, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 0, 2, 1, 1, 1, 1, 2, 0, 0, 1, 0, 2, 2, 0, 0, 2, 1, 0, 2,
                       1, 0, 2, 2, 1, 0, 2, 2, 1, 2, 0, 2, 2, 2, 2, 2, 0, 1, 1, 2, 1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 1,
                       2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 2, 1, 1, 2, 0, 2, 1, 1, 0, 2,
                       0, 0, 1, 2, 0, 0, 1, 2, 2, 2, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 2, 0, 2, 1, 1, 2, 0, 0, 2, 2, 1,
                       0, 2, 1, 2, 2, 0, 0, 1, 2, 1, 0, 2, 1, 1, 0, 0, 1, 2, 2, 0, 1, 1, 2, 2, 0, 0, 0, 2, 0, 1, 2, 1,
                       2, 0, 2, 2, 1, 1, 1, 0, 2, 1, 1, 1, 0, 0, 1, 2, 2, 2, 0, 2, 1, 2, 0, 2, 2, 0, 1, 0, 2, 2, 0, 0,
                       0, 2, 1, 1, 2, 1, 2, 0, 1, 1, 2, 2, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 2, 1, 2, 0, 2, 0,
                       1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 0, 0, 1, 1, 2, 0, 1, 1, 0, 1, 0, 0, 2, 2, 0, 0, 2, 2, 2, 1, 2, 2,
                       1, 0, 2, 2, 2, 1, 0, 2, 0, 1, 0, 0, 0, 1, 0, 1, 2, 1, 2, 1, 2, 1, 0, 2, 0, 0, 1, 0, 2, 1, 1, 2,
                       0, 2, 2, 1, 0, 0, 0, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0, 2, 2, 1, 2, 0, 2, 1, 0, 1, 1,
                       1, 1, 1, 1, 0, 0, 0, 1, 0, 2, 0, 1, 1, 2, 2, 1, 2, 1, 0, 0, 0, 2, 1, 2, 2, 0, 1, 0, 1, 1, 0, 0,
                       0, 0, 0, 2, 0, 1, 0, 0, 1, 2, 0, 1, 2, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0, 2, 0, 2, 2, 1, 2, 2, 1, 0,
                       1, 2, 1, 1, 1, 0, 0, 0, 2, 1, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 0, 0, 2, 0, 1, 2, 1, 1, 0,
                       0, 1, 2, 1, 2, 2, 1, 0, 0, 2, 2, 0, 1, 1, 2, 2, 2, 2, 0, 1, 0, 2, 1, 1, 1, 0, 1, 2, 2, 1, 2, 1,
                       1, 2, 2, 1, 2, 2, 2, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 2, 1, 0, 0, 1, 2, 0, 2,
                       1, 1, 2, 2, 1, 0, 0, 1, 1, 2, 2, 1, 0, 0, 2, 0, 0, 2, 0, 1, 2, 1, 0, 2, 0, 1, 1, 1, 0, 1, 2, 2,
                       2, 1, 0, 0, 2, 1, 2, 0, 0, 0, 1, 0, 2, 2, 1, 0, 0, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 2, 0, 1,
                       1, 0, 2, 2, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 1, 0, 0, 2, 2, 0, 2, 2, 0, 1, 0, 1,
                       0, 2, 1, 1, 2, 1, 1, 0, 2, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 2,
                       1, 2, 2, 1, 0, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 2, 0, 0, 2, 0,
                       1, 1, 2, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 1, 2, 0, 1, 1, 1, 0, 2, 2, 0, 2, 0,
                       1, 2, 0, 2, 0, 0, 2, 1, 1, 1, 0, 2, 1, 2, 1, 2, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1,
                       2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 2, 2, 2, 2, 0, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2, 2,
                       0, 2, 1, 2, 0, 0, 0, 1, 2, 1, 1, 2, 2, 1, 2, 0, 2, 0, 2, 1, 1, 2, 0, 0, 0, 2, 2, 2, 0, 1, 1, 0,
                       0, 0, 2, 1, 0, 2, 2, 2, 1, 0, 2, 2, 0, 0, 1, 2, 0, 1, 1, 2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 0,
                       1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 1, 2, 0, 1, 0, 1,
                       1, 0, 1, 1, 0, 1, 1, 2, 2, 1, 2, 2, 0, 0, 1, 2, 2, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 1, 0, 1, 0,
                       1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 2, 0, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 1, 2, 1, 0, 0, 1, 1, 2, 2, 1,
                       0, 2, 2, 2, 1, 2, 0, 0, 1, 1, 2, 2, 0, 0, 0, 1, 2, 0, 1, 2, 1, 0, 1, 1, 2, 0, 2, 1, 0, 1, 0, 2,
                       1, 2, 0, 1, 0, 2, 2, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 2, 2, 2, 2, 1, 2, 0, 0,
                       1, 2, 2, 2, 1, 0, 2, 0, 2, 1, 1, 1, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 1, 2, 0, 0, 1, 1, 2, 0, 0, 1,
                       2, 2, 0, 1, 1, 1, 2, 0, 0, 2, 0, 2, 2, 0, 2, 1, 2, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 1, 1, 1, 2, 2,
                       1, 1, 1, 0, 0, 1, 0, 0, 2, 1, 1, 2, 2, 1, 2, 1, 0, 2, 2, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0,
                       0, 1, 1, 1, 1, 1, 0, 2, 0, 2, 0, 2, 0, 1, 2, 1, 2, 0, 2, 0, 1, 0, 2, 0, 2, 0, 2, 0, 1, 1, 2, 1,
                       2, 1, 1, 2, 2, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1, 2, 0, 1, 0, 0, 2, 0, 2, 0, 2, 2, 0, 1, 2, 2, 2, 1,
                       1, 0, 2, 1, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 0, 1, 1, 0, 1, 1, 1, 0,
                       2, 1, 1, 2, 0, 2, 0, 1, 2, 2, 0, 0, 1, 0, 1, 2, 1, 2, 0, 2, 1, 1, 0, 2, 2, 0, 1, 0, 1, 0, 0, 0,
                       2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 0, 0, 0, 1,
                       0, 1, 1, 2, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 2, 0, 2, 0, 2, 1, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2,
                       0, 0, 0, 0, 2, 2, 1, 1, 2, 0, 0, 2, 1, 1, 1, 2, 2, 1, 0, 0, 0, 2, 0, 1, 1, 0, 1, 0, 1, 2, 1, 1,
                       0, 1, 1, 2, 2, 1, 0, 0, 2, 2, 1, 1, 1, 2, 0, 0, 0, 2, 1, 2, 1, 1, 2, 1, 0, 1, 2, 0, 2, 2, 0, 2,
                       0, 2, 1, 1, 1, 0, 0, 0, 2, 1, 0, 1, 1, 2, 2, 1, 0, 1, 1, 1, 0, 2, 0, 2, 2, 2, 1, 0, 2, 1, 1, 0,
                       1, 1, 1, 0, 2, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 2, 1, 1, 1, 2, 2, 0, 1, 2, 2, 1, 0, 1,
                       2, 0, 0, 2, 2, 0, 1, 1, 2, 1, 2, 2, 1, 1, 2, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 2, 0, 2, 2, 0,
                       2, 2, 2, 1, 0, 0, 1, 2, 0, 1, 2, 2, 2, 0, 1, 2, 0, 0, 2, 1, 2, 2, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0,
                       0, 2, 2, 2, 1, 2, 2, 2, 2, 0, 2, 1, 0, 0, 0, 1, 2, 2, 1, 0, 1, 1, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0,
                       0, 1, 0, 1, 0, 0, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 2, 1, 2, 2, 1, 1, 1, 1, 0, 2, 2,
                       1, 2, 0, 1, 0, 1, 1, 0, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 0, 1, 0, 1, 0, 1, 0, 0, 2, 1, 1, 1, 2, 1,
                       1, 2, 1, 2, 1, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 1, 1, 2, 1, 1, 1, 0, 2, 1, 0, 0, 2, 0, 2, 2, 1, 1,
                       2, 0, 1, 1, 0, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 1, 2, 0, 0, 1, 2, 0, 0, 0, 2, 2, 1, 2, 2, 2,
                       2, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 2, 0, 2, 1, 0, 2, 0, 1, 2, 0, 2, 2, 1, 0, 1, 1, 1, 2, 1, 1, 1,
                       0, 0, 1, 1, 0, 2, 0, 2, 2, 1, 2, 2, 1, 1, 0, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 0, 0, 1, 0, 1, 2,
                       0, 2, 0, 1, 0, 1, 1, 1, 0, 2, 2, 2, 0, 2, 2, 2, 2, 1, 1, 0, 1, 2, 2, 1, 2, 0, 2, 1, 2, 1, 1, 1,
                       1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 0, 1, 2, 0, 0, 1, 2, 2, 2,
                       1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 0, 1, 1, 2, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0,
                       2, 0, 0, 2, 2, 1, 1, 2, 2, 2, 2, 1, 0, 1, 2, 1, 0, 2, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 2, 0, 1, 0,
                       0, 0, 0, 2, 0, 1, 2, 0, 1, 0, 2, 2, 1, 0, 2, 2, 0, 0, 2, 0, 2, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1,
                       0, 0, 2, 2, 1, 0, 1, 2, 2, 0, 0, 2, 0, 1, 0, 2, 0, 1, 1, 0, 2, 1, 1, 2, 1, 0, 2, 1, 0, 2, 1, 1,
                       0, 2, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 0, 2, 0, 0, 1, 2, 1, 2, 0, 0,
                       1, 0, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 0, 1, 1, 0, 0, 2, 1, 2, 0, 1, 2, 1, 1, 0, 1, 2, 1, 2, 1, 2,
                       2, 1, 2, 2, 1, 2, 0, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 0, 0, 2, 1, 2, 0, 1, 0, 0, 0, 2, 1, 1, 2, 1,
                       0, 2, 1, 1, 2, 2, 1, 0, 0, 0, 0, 1, 2, 0, 1, 0, 1, 2, 2, 1, 0, 1, 2, 0, 1, 1, 2, 2, 2, 0, 1, 0,
                       2, 1, 2, 0, 2, 0, 0, 0, 0, 2, 1, 0, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 0, 0, 2, 2, 1, 1, 0,
                       1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 2, 0, 1, 0, 2, 0, 0, 1, 0, 0, 2, 1, 0, 2, 1, 1, 1, 2, 1, 2, 2, 1,
                       2, 1, 0, 2, 0, 0, 2, 1, 1, 0, 1, 1, 2, 0, 0, 0, 2, 2, 1, 2, 2, 2, 2, 0, 0, 1, 0, 0, 1, 1, 1, 1,
                       1, 2, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 0, 2, 1, 1, 0, 0, 1, 2, 2, 1, 1, 1, 2, 1,
                       0, 0, 2, 0, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 2, 1, 1, 2, 0, 2, 1, 2, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1,
                       0, 2, 2, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 0, 1, 2, 1, 0, 0, 2, 0, 0, 0, 2, 2, 2, 1, 2, 2, 1, 2, 0,
                       0, 1, 0, 1, 0, 2, 2, 2, 0, 2, 0, 2, 0, 1, 1, 0, 0, 0, 0, 2, 1, 0, 2, 1, 1, 1, 0, 1, 0, 2, 1, 2,
                       2, 1, 0, 2, 2, 1, 2, 2, 1, 1, 1, 2, 1, 0, 0, 0, 0, 2, 2, 1, 1, 2, 0, 1, 2, 2, 1, 1, 1, 1, 0, 0,
                       1, 1, 1, 0, 0, 2, 1, 2, 0, 1, 1, 1, 2, 1, 0, 2, 1, 1, 1, 2, 1, 1, 0, 0, 1, 2, 2, 0, 0, 0, 1, 0,
                       1, 0, 1, 2, 0, 2, 2, 2, 2, 1, 1, 0, 1, 1, 1, 2, 0, 2, 0, 1, 2, 0, 0, 1, 2, 2, 1, 2, 2, 1, 0, 0,
                       0, 0, 0, 2, 2, 1, 1, 1, 1, 2, 0, 1, 2, 2, 2, 2, 0, 0, 1, 2, 2, 2, 2, 0, 0, 0, 2, 1, 0, 0, 1, 2,
                       1, 0, 1, 2, 1, 2, 1, 0, 2, 1, 0, 0, 2, 0, 2, 1, 1, 1, 0, 0, 0, 1, 2, 1, 1, 0, 0, 1, 1, 0, 0, 1,
                       0, 0, 0, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 1, 1, 1, 0, 2, 2, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 2,
                       1, 0, 1, 0, 2, 2, 1, 0, 2, 1, 2, 1, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 1, 2, 1, 2, 1, 0, 0, 2, 0, 2,
                       1, 1, 1, 2, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 1, 2, 2, 0, 2, 0, 2, 0, 2, 1, 2, 0, 1, 1, 1, 1, 0, 2,
                       0, 1, 0, 2, 0, 2, 2, 0, 2, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 0, 0, 2, 0, 2, 2,
                       0, 2, 2, 2, 0, 0, 1, 1, 0, 1, 0, 0, 1, 2, 1, 1, 1, 0, 1, 0, 0, 1, 0, 2, 1, 1, 1, 0, 0, 2, 1, 2,
                       2, 0, 0, 1, 2, 1, 0, 2, 2, 0, 1, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 1, 2, 1, 2, 2, 0, 0, 0, 1, 1,
                       0, 1, 1, 0, 2, 2, 0, 0, 2, 2, 0, 1, 0, 2, 1, 2, 0, 0, 1, 2, 1, 2, 2, 0, 0, 2, 2, 0, 2, 1, 2, 2,
                       1, 2, 2, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 2, 1, 1, 0, 0, 0, 2, 2, 1, 0, 0, 1, 2, 0, 2, 1, 2, 1, 2,
                       1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 0, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 2,
                       2, 2, 0, 2, 0, 0, 0, 1, 1, 1, 0, 2, 1, 2, 1, 2, 2, 2, 2, 0, 1, 2, 2, 1, 2, 1, 2, 2, 1, 0, 0, 0,
                       2, 2, 2, 1, 1, 0, 1, 1, 2, 0, 0, 2, 1, 2, 2, 2, 2, 2, 0, 2, 1, 1, 2, 1, 1, 2, 0, 0, 1, 2, 1, 2,
                       0, 2, 0, 0, 2, 2, 2, 0, 2, 0, 0, 1, 1, 2, 2, 2, 0, 2, 0, 2, 1, 1, 0, 0, 0, 2, 0, 0, 1, 1, 2, 2,
                       0, 1, 0, 1, 0, 0, 2, 2, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 2, 2, 1, 0, 1, 2, 0, 0, 2,
                       2, 2, 0, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 0, 2, 2, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0,
                       2, 2, 0, 1, 2, 2, 0, 0, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 0, 0, 0, 2, 2, 1, 2, 0, 0, 2, 2, 1, 1, 2,
                       2, 1, 2, 2, 0, 0, 1, 0, 2, 2, 1, 1, 2, 0, 0, 1, 2, 1, 1, 1, 1, 0, 2, 2, 0, 2, 1, 1, 0, 1, 1, 1,
                       1, 2, 0, 0, 2, 2, 0, 1, 1, 1, 0, 2, 2, 1, 2, 0, 0, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 0, 1, 2,
                       1, 2, 2, 0, 1, 0, 1, 1, 1, 2, 0, 0, 0, 1, 2, 1, 2, 0, 0, 2, 0, 1, 1, 2, 0, 1, 1, 0, 1, 1, 0, 0,
                       2, 2, 1, 0, 2, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 2, 1, 1, 0, 2, 0, 1, 1, 0, 2, 0, 2, 0, 0, 0, 2, 2,
                       2, 0, 2, 2, 1, 1, 0, 0, 2, 0, 1, 2, 1, 0, 2, 2, 0, 2, 0, 0, 0, 2, 1, 0, 2, 1, 2, 0, 1, 0, 0, 0,
                       1, 1, 1, 2, 1, 2, 1, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, 1, 2, 2, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0,
                       2, 0, 0, 2, 2, 2, 1, 0, 2, 2, 0, 2, 1, 0, 2, 0, 1, 0, 0, 1, 1, 2, 2, 1, 0, 2, 1, 2, 0, 0, 0, 2,
                       0, 1, 0, 2, 1, 2, 0, 2, 0, 1, 2, 2, 0, 1, 1, 2, 0, 1, 0, 2, 2, 0, 2, 2, 2, 1, 0, 0, 0, 0, 2, 1,
                       1, 0, 1, 0, 0, 0, 2, 1, 1, 0, 2, 2, 2, 1, 2, 0, 1, 1, 1, 1, 0, 1, 0, 0, 2, 1, 1, 2, 1, 2, 1, 1,
                       2, 2, 2, 2, 2, 1, 1, 2, 0, 0, 1, 1, 0, 2, 0, 2, 1, 2, 2, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 2, 2,
                       0, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 0, 1, 2, 2, 2, 1, 2, 0, 2, 0, 2,
                       2, 0, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 0, 0, 2, 1, 2, 0, 0, 0, 1, 1, 0, 1, 2, 1, 1, 2, 1, 1, 0, 2,
                       0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 2, 0, 1, 2, 1, 0, 1, 2, 2, 0, 0, 2, 1, 2, 2, 2, 1, 2, 1,
                       0, 1, 1, 0, 0, 0, 2, 0, 0, 1, 2, 0, 2, 2, 1, 2, 0, 1, 2, 0, 1, 1, 2, 2, 2, 0, 1, 1, 1, 2, 1, 2,
                       2, 2, 2, 1, 1, 0, 0, 2, 0, 2, 0, 0, 0, 1, 1, 0, 2, 2, 1, 0, 2, 1, 1, 2, 1, 0, 1, 1, 0, 1, 1, 0,
                       2, 2, 2, 0, 2, 0, 1, 1, 1, 2, 1, 0, 1, 2, 0, 1, 1, 2, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 2, 1, 1, 0,
                       0, 2, 1, 1, 2, 1, 0, 2, 1, 1, 1, 1, 0, 1, 1, 2, 1, 2, 1, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 2, 0, 1,
                       2, 2, 1, 0, 0, 1, 1, 0, 2, 2, 1, 0, 2, 2, 2, 2, 2, 1, 0, 0, 2, 2, 2, 1, 0, 2, 2, 0, 1, 1, 2, 2,
                       1, 1, 2, 2, 0, 1, 0, 0, 1, 1, 2, 2, 1, 0, 0, 2, 1, 2, 0, 1, 1, 1, 1, 0, 2, 0, 0, 0, 2, 0, 2, 2,
                       0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 2, 1, 1, 0, 0, 1, 0, 2, 2, 0, 0, 1, 2, 1, 1, 0,
                       2, 2, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 2, 2, 0, 0, 0, 0, 2, 0, 1, 0, 1,
                       2, 0, 0, 0, 1, 0, 0, 1, 1, 1, 2, 2, 1, 1, 2, 1, 0, 1, 0, 2, 2, 1, 0, 1, 0, 2, 2, 0, 0, 2, 1, 0,
                       0, 2, 1, 0, 1, 0, 1, 2, 1, 0, 0, 2, 2, 1, 0, 2, 0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 1, 0, 2, 2, 0, 0,
                       2, 2, 2, 1, 1, 2, 2, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 2, 1, 2, 2, 0, 2, 1, 2, 2, 2, 1, 2, 0, 2,
                       0, 2, 1, 0, 2, 2, 0, 1, 0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 2, 1, 2, 2, 0, 1, 1, 0, 0, 1, 0, 2, 0, 2,
                       0, 2, 1, 1, 0, 2, 0, 0, 0, 2, 2, 1, 0, 2, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 0, 1, 0, 1, 0, 1,
                       2, 1, 0, 0, 0, 0, 1, 2, 0, 2, 0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 0, 1, 0, 2, 1, 2, 0, 0, 0, 1,
                       2, 2, 2, 0, 0, 2, 1, 0, 2, 0, 1, 2, 1, 2, 2, 2, 0, 1, 0, 0, 0, 1, 2, 1, 1, 1, 0, 0, 1, 1, 2, 0,
                       1, 0, 2, 1, 0, 2, 0, 0, 2, 1, 1, 1, 2, 2, 2, 0, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2,
                       1, 2, 0, 2, 1, 2, 0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 2, 1, 2, 1, 0, 1, 2, 2, 2,
                       2, 1, 1, 1, 0, 1, 2, 0, 0, 1, 1, 0, 0, 1, 2, 0, 2, 2, 0, 0, 0, 0, 2, 1, 1, 2, 1, 1, 2, 2, 0, 2,
                       2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 2, 1, 2, 1, 1, 0, 0, 1, 2, 2, 0, 1, 2, 1, 2, 2, 1, 1,
                       0, 1, 0, 2, 0, 2, 2, 1, 2, 2, 2, 2, 2, 0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 2, 1, 2, 2, 1,
                       0, 0, 1, 0, 0, 0, 1, 0, 1, 2, 2, 0, 1, 2, 0, 2, 2, 2, 2, 1, 2, 1, 2, 2, 0, 2, 1, 2, 0, 0, 0, 0,
                       1, 1, 2, 1, 0, 2, 0, 2, 0, 2, 1, 2, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 0, 2, 1, 0, 1, 1, 0, 1, 0,
                       0, 2, 0, 2, 2, 0, 1, 2, 2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 2, 2, 1, 2, 2, 1, 1, 0, 1, 1, 0, 0, 2, 2,
                       1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 2, 0, 2, 0, 1, 0, 2, 0, 0, 0, 1, 2, 1, 2, 1, 1,
                       0, 0, 2, 2, 2, 2, 1, 0, 0, 2, 0, 1, 2, 2, 2, 2, 0, 1, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 0, 2, 0, 1,
                       2, 1, 2, 0, 2, 2, 1, 0, 2, 1, 0, 2, 1, 2, 0, 2, 1, 0, 2, 1, 1, 0, 1, 2, 2, 2, 1, 1, 1, 2, 1, 1,
                       1, 1, 0, 2, 1, 2, 1, 1, 2, 1, 0, 2, 0, 1, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 2, 2, 0, 0, 0, 2, 1, 2,
                       2, 2, 0, 1, 1, 2, 1, 2, 0, 0, 0, 2, 1, 1, 0, 1, 0, 1, 0, 2, 2, 1, 2, 0, 1, 1, 1, 2, 2, 0, 1, 2,
                       1, 2, 2, 0, 1, 2, 1, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 2, 0, 1, 2, 2, 0, 2, 1, 0, 2, 1, 1, 2, 0, 0,
                       2, 1, 0, 1, 2, 2, 2, 2, 0, 0, 1, 2, 1, 0, 2, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 0, 0,
                       2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 2, 2, 1, 2, 1, 1, 1, 2, 2, 0, 2, 0, 2, 0, 0, 1, 0,
                       2, 0, 0, 2, 0, 0, 1, 1, 0, 2, 0, 1, 2, 0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1,
                       1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 1, 1, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1,
                       1, 2, 0, 0, 1, 2, 2, 2, 1, 0, 2, 2, 1, 0, 1, 1, 2, 2, 0, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 0, 2, 1,
                       0, 2, 1, 2, 1, 0, 1, 2, 2, 2, 0, 0, 1, 1, 2, 0, 2, 2, 2, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 2, 1, 2,
                       1, 2, 1, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 2, 0, 0, 1, 1,
                       1, 0, 1, 2, 2, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 1, 0, 2, 1, 1, 0, 2, 1, 0, 1, 0, 0, 2,
                       1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 2, 0, 0, 1, 0, 2, 2, 1, 1, 2, 2, 1, 0, 0, 2, 2, 0, 2, 1, 1, 2, 1,
                       1, 1, 0, 2, 0, 0, 0, 2, 1, 2, 0, 0, 0, 2, 2, 1, 2, 1, 1, 1, 2, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 2,
                       1, 0, 1, 0, 1, 1, 1, 0, 2, 1, 0, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 1,
                       2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 1, 0, 0, 1, 1, 2, 0, 2, 2, 1, 1, 1, 0, 2, 1, 1, 2, 2, 1, 2, 1, 1,
                       2, 2, 0, 2, 2, 0, 1, 2, 2, 2, 0, 0, 1, 2, 1, 1, 0, 1, 2, 1, 1, 2, 2, 1, 2, 2, 0, 0, 2, 0, 0, 1,
                       0, 0, 2, 2, 1, 2, 0, 1, 2, 0, 1, 2, 0, 0, 1, 0, 2, 1, 1, 0, 2, 0, 2, 0, 2, 1, 2, 1, 2, 1, 2, 2,
                       0, 2, 2, 1, 0, 2, 2, 1, 2, 2, 1, 1, 1, 1, 0, 0, 1, 2, 1, 2, 1, 0, 1, 0, 2, 1, 0, 1, 1, 1, 0, 0,
                       2, 2, 0, 2, 1, 2, 0, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 1, 2, 2, 2, 1, 0, 1,
                       1, 2, 2, 2, 0, 1, 1, 0, 0, 1, 1, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0,
                       2, 0, 1, 1, 0, 2, 1, 1, 2, 1, 1, 0, 0, 0, 1, 2, 0, 0, 1, 0, 2, 0, 2, 1, 2, 2, 1, 0, 0, 0, 1, 1,
                       1, 2, 1, 0, 0, 2, 1, 1, 2, 0, 0, 1, 2, 2, 1, 1, 0, 1, 1, 2, 0, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1,
                       1, 0, 1, 1, 0, 1, 2, 0, 1, 0, 1, 1, 1, 0, 1, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1, 2, 2, 0, 1, 2, 0, 1,
                       2, 2, 0, 0, 0, 1, 0, 2, 0, 1, 2, 1, 2, 0, 0, 1, 1, 1, 2, 0, 0, 1, 1, 1, 2, 0, 2, 1, 1, 2, 2, 2,
                       2, 1, 1, 2, 0, 0, 0, 2, 2, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 2, 1,
                       0, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 0, 2, 0, 2, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0, 1, 1, 1, 1, 2, 2,
                       1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 0, 0, 1, 0, 1, 1, 2, 0, 2, 0, 2, 1, 1, 1, 1, 1, 2, 2, 0, 0, 0,
                       1, 1, 0, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0, 1, 2, 2, 2, 1, 0, 2, 2, 2, 1, 1, 2, 2, 0, 2, 0, 1, 2, 0,
                       0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 2, 0, 0, 2, 2,
                       2, 1, 2, 2, 1, 2, 0, 1, 0, 0, 2, 1, 2, 1, 2, 1, 1, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0,
                       1, 2, 0, 0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 0, 2, 2, 0, 2, 1, 2, 0, 2, 1, 0, 2, 2, 1, 2, 0, 2, 0,
                       2, 2, 1, 1, 2, 0, 2, 0, 0, 0, 2, 2, 1, 1, 0, 2, 2, 2, 1, 0, 1, 0, 0, 0, 2, 0, 2, 2, 2, 1, 0, 0,
                       2, 0, 0, 2, 1, 2, 2, 0, 2, 2, 0, 2, 2, 2, 1, 2, 0, 0, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 0, 2, 2, 1,
                       1, 1, 2, 1, 0, 2, 0, 2, 1, 0, 2, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 2, 1, 2, 1, 0, 1, 1, 0, 2, 1, 0,
                       0, 1, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2, 0, 2, 1, 1, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 2,
                       0, 1, 2, 0, 2, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 2, 0, 2, 1, 2, 1, 2, 0, 2, 0, 0, 2, 2, 1, 0,
                       2, 2, 2, 1, 2, 2, 0, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 0, 1, 0, 1, 2, 2, 0, 1, 2, 1, 0, 1, 1,
                       1, 0, 1, 0, 2, 2, 1, 2, 1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 1, 0, 1,
                       0, 2, 0, 0, 2, 2, 1, 0, 1, 0, 0, 2, 2, 0, 1, 0, 0, 1, 0, 2, 2, 0, 1, 2, 0, 0, 1, 1, 2, 0, 1, 1,
                       2, 0, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 2, 2, 0, 0, 2, 0, 1, 0, 2, 0, 2, 2, 1, 1, 2, 2, 2, 1, 0, 2,
                       0, 0, 2, 2, 1, 2, 0, 2, 1, 0, 2, 1, 2, 0, 1, 0, 2, 0, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 1, 1, 1, 2,
                       2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 2, 2, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 1, 1, 0,
                       1, 1, 2, 2, 0, 1, 0, 2, 0, 1, 2, 1, 1, 1, 0, 0, 2, 0, 0, 2, 2, 1, 0, 2, 1, 0, 1, 1, 0, 2, 0, 0,
                       0, 1, 1, 0, 1, 2, 2, 1, 1, 1, 2, 2, 2, 1, 0, 2, 0, 1, 1, 1, 2, 2, 0, 1, 0, 0, 2, 2, 1, 1, 1, 1,
                       2, 2, 0, 1, 0, 0, 0, 2, 1, 1, 2, 2, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 2, 1, 1, 0, 1, 1, 0, 2, 2,
                       0, 0, 0, 2, 2, 0, 2, 0, 2, 2, 2, 1, 0, 1, 1, 2, 0, 2, 0, 0, 2, 2, 1, 1, 2, 2, 1, 1, 1, 0, 1, 0,
                       0, 1, 1, 1, 0, 1, 2, 1, 1, 0, 0, 0, 2, 2, 0, 0, 1, 2, 2, 1, 0, 2, 2, 0, 1, 2, 2, 1, 1, 2, 1, 0,
                       2, 2, 1, 1, 1, 0, 2, 2, 0, 2, 2, 1, 0, 1, 0, 1, 0, 2, 0, 2, 1, 2, 0, 0, 0, 2, 0, 1, 2, 1, 2, 2,
                       2, 2, 1, 0, 2, 1, 2, 0, 0, 0, 1, 1, 2, 2, 0, 2, 1, 1, 0, 2, 2, 0, 1, 1, 0, 2, 2, 1, 1, 2, 2, 2,
                       0, 2, 0, 1, 2, 0, 0, 0, 0, 2, 2, 0, 0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 2, 2, 1, 1, 1, 1, 0, 2, 0, 2,
                       1, 0, 2, 1, 0, 0, 2, 0, 2, 1, 0, 1, 1, 0, 2, 1, 1, 2, 1, 0, 2, 0, 2, 0, 1, 1, 2, 1, 0, 2, 0, 2,
                       2, 1, 0, 1, 1, 1, 2, 2, 1, 2, 1, 0, 0, 0, 1, 1, 0, 2, 1, 0, 1, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
                       2, 0, 2, 2, 1, 2, 2, 2, 2, 0, 1, 2, 0, 2, 2, 2, 2, 1, 2, 1, 0, 2, 1, 1, 1, 0, 2, 1, 0, 2, 2, 2,
                       0, 0, 2, 1, 0, 1, 2, 2, 1, 2, 1, 1, 0, 2, 1, 1, 0, 1, 0, 2, 2, 0, 2, 0, 1, 1, 1, 1, 1, 0, 2, 0,
                       0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 1, 1, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 2, 1, 0,
                       2, 2, 1, 1, 1, 2, 0, 0, 0, 2, 2, 1, 0, 1, 2, 1, 1, 2, 0, 2, 0, 0, 0, 0, 2, 0, 0, 1, 1, 2, 1, 2,
                       1, 2, 1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1, 1, 0, 0, 2, 0, 0, 1, 2, 0, 1, 2, 1,
                       1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 2, 0, 2, 0, 1, 0, 0, 1, 2, 0, 1, 0, 1, 0, 2, 2, 1, 0, 1, 1, 0, 1,
                       2, 2, 1, 2, 1, 2, 2, 1, 1, 0, 2, 0, 1, 2, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 2, 1, 1, 0, 1, 0, 1, 1,
                       2, 1, 2, 1, 0, 2, 1, 2, 1, 1, 1, 0, 2, 0, 1, 2, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 2, 2, 0, 1, 1, 1,
                       1, 2, 0, 2, 0, 0, 1, 2, 2, 2, 2, 0, 2, 0, 1, 2, 2, 0, 1, 2, 0, 1, 0, 0, 1, 1, 1, 2, 0, 2, 2, 2,
                       2, 0, 2, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 2, 0, 1, 0, 0, 2, 2, 1, 1, 0, 1, 2, 2, 2, 1, 1, 1,
                       1, 1, 1, 2, 1, 2, 0, 2, 2, 2, 1, 1, 1, 0, 1, 1, 1, 1, 0, 2, 1, 2, 0, 0, 2, 1, 2, 0, 2, 2, 2, 0,
                       0, 2, 1, 0, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 0, 0, 1, 1, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 2, 1,
                       0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 1, 1, 1, 2, 2, 0, 0, 1, 1, 2, 0, 1, 0, 1, 0, 0, 2, 1, 2, 2, 1,
                       1, 0, 1, 0, 2, 2, 2, 0, 2, 0, 0, 2, 0, 1, 0, 0, 0, 1, 1, 2, 0, 0, 0, 2, 1, 1, 0, 2, 1, 0, 1, 0,
                       1, 2, 2, 1, 0, 2, 2, 2, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 2, 0,
                       1, 1, 1, 1, 0, 0, 0, 2, 1, 0, 0, 2, 2, 2, 0, 0, 1, 2, 2, 2, 1, 2, 1, 2, 0, 2, 0, 1, 0, 0, 2, 0,
                       1, 0, 2, 1, 2, 1, 2, 2, 1, 0, 1, 1, 0, 1, 2, 1, 2, 1, 0, 0, 2, 2, 1, 0, 0, 1, 1, 2, 1, 1, 2, 1,
                       1, 1, 2, 2, 1, 0, 0, 2, 1, 1, 0, 2, 1, 2, 0, 2, 0, 1, 2, 2, 2, 0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1,
                       0, 1, 1, 1, 1, 0, 1, 1, 0, 2, 0, 0, 1, 2, 1, 2, 0, 1, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 2, 1, 1, 2,
                       1, 1, 0, 1, 0, 2, 0, 0, 0, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 0, 2, 0, 2, 2, 1, 0, 0, 2,
                       0, 2, 2, 2, 0, 1, 2, 2, 1, 0, 2, 1, 1, 2, 1, 1, 2, 0, 1, 0, 0, 1, 1, 0, 0, 1, 2, 2, 1, 2, 0, 2,
                       2, 2, 1, 1, 2, 1, 1, 0, 2, 0, 1, 0, 0, 2, 0, 2, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 1, 2, 1, 0, 0, 1,
                       2, 0, 1, 1, 0, 2, 1, 1, 0, 2, 1, 2, 2, 2, 2, 0, 2, 1, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 1, 1, 2, 0,
                       2, 2, 0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 1, 2, 0, 2, 0, 0, 0, 2, 0, 1, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2,
                       0, 1, 2, 0, 0, 2, 1, 0, 1, 2, 1, 2, 1, 0, 1, 1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 1, 2,
                       1, 2, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 2, 1, 2, 0, 1, 1, 1, 1, 0, 1, 0, 0, 2, 1, 2, 1, 2, 2,
                       0, 1, 0, 1, 1, 2, 1, 0, 1, 0, 1, 1, 2, 2, 0, 2, 0, 1, 0, 2, 0, 1, 1, 2, 0, 1, 1, 1, 0, 2, 0, 1,
                       2, 1, 1, 2, 2, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 2, 1, 2, 0, 2, 1, 2, 1, 2, 2, 0, 1, 1, 2, 1, 1,
                       1, 2, 1, 1, 0, 0, 2, 0, 2, 1, 1, 0, 0, 2, 0, 2, 0, 2, 2, 1, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0,
                       2, 2, 2, 0, 0, 2, 1, 1, 2, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 2, 2, 2, 2, 0, 2, 1, 1, 1, 0, 1,
                       2, 2, 2, 1, 0, 0, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 2, 1, 2, 2, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 2, 1,
                       1, 1, 1, 0, 1, 1, 0, 0, 2, 0, 0, 2, 1, 2, 2, 2, 0, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 2, 2, 1, 1,
                       1, 2, 0, 2, 2, 2, 2, 0, 0, 0, 2, 1, 1, 1, 0, 0, 2, 1, 2, 0, 1, 0, 0, 2, 2, 1, 0, 0, 1, 2, 1, 2,
                       0, 2, 0, 1, 0, 0, 2, 0, 0, 1, 2, 2, 0, 0, 2, 0, 2, 2, 0, 1, 1, 0, 2, 0, 1, 0, 0, 1, 2, 1, 2, 0,
                       0, 2, 0, 2, 1, 2, 2, 1, 2, 1, 1, 2, 1, 2, 2, 0, 1, 2, 0, 2, 1, 0, 1, 0, 2, 2, 1, 0, 2, 0, 0, 2,
                       0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 0,
                       2, 2, 2, 0, 2, 2, 1, 0, 2, 1, 2, 1, 2, 2, 2, 1, 1, 0, 2, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1,
                       2, 1, 2, 1, 0, 1, 2, 2, 2, 1, 0, 2, 1, 0, 1, 2, 1, 0, 0, 1, 2, 0, 2, 0, 1, 1, 0, 1, 2, 0, 2, 0,
                       1, 2, 1, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 2, 0, 1, 0, 1, 2, 0, 0, 0, 2, 1, 1, 2, 2, 2, 1, 2, 0,
                       1, 1, 0, 2, 0, 0, 2, 2, 2, 0, 0, 2, 2, 1, 2, 2, 2, 0, 2, 0, 1, 0, 0, 1, 1, 0, 2, 1, 2, 1, 1, 1,
                       0, 0, 2, 1, 0, 0, 1, 2, 0, 2, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 0, 2, 2, 1, 0, 1, 2, 2, 0, 2, 2, 1,
                       0, 1, 2, 0, 2, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 2, 1, 2, 0, 1, 2, 2, 2, 0,
                       2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 1, 0, 1, 2, 0,
                       0, 0, 0, 2, 0, 1, 2, 0, 1, 0, 1, 1, 0, 2, 0, 1, 0, 0, 1, 2, 2, 0, 0, 2, 2, 2, 1, 0, 2, 2, 0, 2,
                       1, 2, 2, 0, 2, 0, 0, 2, 0, 1, 2, 2, 2, 2, 0, 1, 0, 2, 2, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0,
                       2, 2, 1, 1, 2, 1, 2, 1, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1, 1, 0, 2,
                       0, 2, 0, 2, 1, 2, 0, 1, 1, 0, 2, 1, 1, 2, 0, 0, 1, 0, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0,
                       0, 2, 1, 0, 1, 0, 1, 0, 1, 2, 2, 1, 0, 1, 0, 1, 2, 0, 1, 0, 0, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 0,
                       0, 2, 0, 0, 0, 2, 1, 1, 2, 1, 1, 0, 1, 0, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 1, 1, 0, 1, 2, 2,
                       2, 2, 0, 1, 2, 2, 2, 0, 1, 0, 2, 2, 2, 0, 0, 1, 2, 0, 0, 1, 1, 0, 2, 1, 2, 0, 1, 0, 1, 1, 2, 1,
                       0, 1, 0, 1, 0, 2, 2, 2, 1, 1, 1, 0, 0, 1, 2, 0, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 2, 0, 0, 1,
                       1, 0, 2, 1, 2, 1, 1, 2, 1, 2, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 2, 2, 1, 1, 2, 1, 1, 2, 0, 1, 0, 0,
                       0, 2, 0, 1, 0, 2, 2, 2, 2, 0, 1, 2, 1, 1, 0, 1, 1, 2, 2, 1, 0, 2, 0, 1, 2, 1, 2, 1, 1, 1, 1, 0,
                       0, 1, 0, 1, 2, 2, 0, 1, 1, 1, 0, 1, 1, 2, 1, 0, 2, 1, 1, 0, 1, 1, 2, 2, 1, 2, 0, 0, 1, 0, 2, 0,
                       1, 1, 1, 0, 0, 0, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 1, 0, 1, 2, 0, 0, 1, 1, 0, 2, 1, 2, 2, 1, 1, 2,
                       2, 2, 1, 2, 0, 1, 2, 2, 1, 1, 2, 2, 0, 1, 0, 0, 0, 1, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2,
                       1, 2, 2, 1, 2, 2, 0, 2, 1, 2, 1, 2, 1, 1, 2, 0, 1, 0, 0, 0, 2, 2, 2, 1, 2, 0, 0, 2, 0, 2, 0, 0,
                       2, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 2, 0, 1, 1, 0,
                       1, 2, 2, 2, 2, 1, 0, 2, 2, 0, 1, 1, 2, 1, 2, 0, 2, 1, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0,
                       1, 1, 2, 2, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 1, 0, 1, 1, 1, 1, 0, 2, 1, 1,
                       1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 0, 1, 0, 1, 1, 2, 1, 1, 2, 0, 0, 1, 2, 1, 1, 0, 1, 1, 2, 2, 1,
                       1, 0, 2, 1, 2, 0, 2, 1, 1, 0, 2, 1, 2, 0, 1, 0, 2, 0, 0, 1, 2, 0, 1, 2, 1, 2, 2, 1, 0, 0, 0, 0,
                       1, 1, 2, 1, 2, 2, 0, 1, 2, 2, 0, 0, 1, 2, 0, 1, 2, 0, 2, 2, 0, 2, 1, 0, 1, 1, 0, 2, 0, 1, 2, 0,
                       2, 0, 1, 0, 0, 2, 1, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 2, 2, 0, 1, 1, 1, 2, 2, 0, 2, 0, 1, 2, 1,
                       1, 0, 1, 0, 0, 1, 2, 2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 1, 1, 1, 1, 0, 2,
                       0, 2, 2, 0, 2, 1, 0, 1, 0, 1, 1, 1, 0, 2, 0, 1, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 2, 2, 0, 2, 2, 0,
                       0, 0, 0, 2, 1, 2, 0, 1, 1, 2, 2, 2, 1, 0, 2, 1, 0, 2, 0, 2, 0, 2, 0, 1, 2, 1, 1, 0, 2, 2, 1, 0,
                       1, 2, 2, 1, 2, 0, 1, 1, 2, 1, 1, 2, 0, 1, 2, 0, 0, 2, 0, 1, 2, 0, 2, 2, 0, 2, 0, 1, 2, 1, 2, 2,
                       2, 0, 2, 1, 2, 0, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 1, 1, 0, 2, 0, 2, 2, 2, 0, 2, 0, 1, 2, 0, 0, 0,
                       2, 2, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2, 0, 1, 2, 2, 2, 2, 0, 2, 1, 1, 0,
                       1, 2, 0, 0, 2, 1, 1, 1, 0, 2, 0, 2, 0, 2, 2, 0, 1, 0, 1, 0, 1, 0, 2, 2, 1, 0, 2, 2, 0, 0, 2, 1,
                       0, 2, 0, 0, 1, 0, 0, 2, 1, 1, 0, 1, 2, 1, 0, 2, 1, 2, 2, 2, 1, 2, 0, 1, 0, 1, 2, 1, 1, 2, 0, 1,
                       2, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 2, 1, 2, 1, 0, 1, 1, 2, 2, 2, 1, 0, 0, 1, 0, 1, 1, 2, 0, 0, 1,
                       2, 2, 0, 0, 2, 2, 0, 1, 2, 0, 0, 2, 2, 2, 2, 0, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2,
                       1, 0, 1, 0, 2, 1, 2, 0, 0, 2, 2, 0, 2, 2, 0, 0, 1, 1, 2, 1, 2, 2, 2, 0, 1, 1, 0, 0, 2, 0, 0, 2,
                       0, 1, 2, 2, 2, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2, 2, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1,
                       0, 2, 1, 1, 0, 0, 2, 1, 0, 0, 0, 1, 0, 2, 1, 1, 2, 2, 0, 1, 0, 2, 1, 2, 1, 2, 1, 2, 2, 0, 0, 0,
                       0, 2, 0, 1, 2, 1, 2, 0, 2, 1, 0, 1, 2, 2, 2, 0, 2, 0, 1, 1, 0, 2, 1, 2, 2, 1, 2, 2, 0, 1, 2, 2,
                       1, 1, 0, 1, 1, 0, 2, 1, 0, 1, 0, 0, 1, 2, 0, 2, 1, 1, 2, 0, 2, 0, 0, 2, 1, 0, 2, 1, 1, 1, 1, 1,
                       2, 2, 2, 0, 2, 0, 0, 0, 1, 0, 0, 1, 2, 2, 1, 0, 2, 2, 1, 2, 1, 1, 1, 1, 0, 1, 0, 2, 2, 0, 1, 2,
                       2, 0, 0, 2, 1, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 2, 0, 2, 1, 1, 0, 0, 1, 2, 2, 2, 1, 0, 0, 1, 1, 1,
                       1, 0, 2, 1, 1, 1, 2, 2, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 1, 2, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
                       0, 0, 1, 1, 1, 0, 0, 1, 2, 2, 0, 2, 0, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 0, 2,
                       1, 1, 0, 2, 2, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 2, 0, 1, 1, 1, 1, 0, 2, 2, 2, 1, 0, 1, 0, 1, 2, 1,
                       2, 0, 0, 1, 2, 1, 0, 1, 2, 0, 0, 1, 1, 2, 2, 1, 1, 2, 1, 0, 2, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 0,
                       1, 0, 0, 2, 0, 1, 2, 1, 0, 2, 2, 2, 0, 2, 1, 1, 1, 0, 0, 0, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 1, 0,
                       2, 1, 1, 1, 0, 2, 2, 1, 0, 2, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 2, 2, 1, 0, 1, 1, 1, 2, 1, 1, 0, 1,
                       0, 2, 0, 0, 0, 1, 0, 0, 2, 2, 2, 1, 1, 1, 1, 2, 1, 0, 2, 0, 1, 2, 2, 1, 1, 0, 2, 1, 1, 1, 0, 2,
                       2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 2, 1,
                       0, 1, 2, 1, 2, 0, 2, 0, 2, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 2, 1, 2, 2,
                       2, 1, 2, 2, 2, 2, 1, 0, 2, 1, 1, 0, 0, 2, 1, 1, 1, 2, 1, 0, 2, 1, 2, 1, 2, 1, 2, 0, 2, 0, 1, 0,
                       1, 2, 0, 0, 2, 1, 1, 2, 1, 2, 0, 2, 2, 2, 1, 1, 0, 0, 0, 2, 1, 2, 2, 1, 2, 0, 0, 1, 0, 0, 0, 1,
                       1, 0, 0, 1, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 1, 1, 0, 2,
                       2, 1, 2, 2, 1, 1, 2, 2, 1, 0, 0, 0, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 0, 2, 0, 0, 0, 0, 0, 1,
                       0, 1, 0, 2, 0, 1, 1, 1, 1, 0, 0, 1, 2, 2, 0, 2, 1, 1, 1, 0, 1, 1, 2, 2, 0, 1, 2, 2, 1, 1, 1, 0,
                       1, 1, 0, 0, 0, 0, 2, 1, 0, 2, 1, 1, 0, 0, 0, 0, 2, 0, 1, 0, 0, 1, 1, 1, 1, 0, 2, 2, 0, 2, 2, 2,
                       1, 0, 2, 1, 1, 0, 1, 0, 1, 2, 0, 2, 0, 2, 0, 2, 2, 0, 0, 1, 2, 0, 1, 1, 1, 0, 1, 0, 2, 0, 0, 2,
                       2, 2, 1, 0, 1, 2, 0, 1, 2, 2, 1, 0, 0, 1, 0, 1, 0, 2, 1, 0, 2, 1, 2, 2, 0, 1, 1, 1, 1, 2, 1, 2,
                       1, 0, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 0, 1, 2, 0, 1, 2, 2, 0, 2, 2, 2, 1, 0, 2, 0, 1, 2,
                       2, 0, 1, 2, 0, 1, 2, 1, 1, 2, 0, 1, 2, 2, 0, 2, 1, 1, 0, 0, 2, 0, 2, 2, 1, 1, 0, 0, 0, 1, 1, 1,
                       0, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 1, 2, 0, 2, 1, 2, 1, 2, 0, 0, 2, 2, 1, 1,
                       0, 1, 2, 1, 0, 1, 0, 0, 2, 0, 2, 0, 0, 1, 2, 2]


    flag1 = flag[:]
    flag2 = flag[:]



    t1 = time.time()
    flag2.sort()
    t2 = time.time()
    print(t2 - t1)

    t1 = time.time()
    flag_sort(flag1)
    t2 = time.time()
    print(t2 - t1)




    # long_list = []
    # for i in range(10000):
    #     long_list.append(random.randint(0, 2))
    # print(long_list)


if __name__ == '__main__':
    main()
