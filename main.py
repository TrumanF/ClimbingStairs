import sys
import math
sys.setrecursionlimit(2000)
steps = [1, 2]
results = {}


def climb_stairs(no_stairs):
    if no_stairs in results:
        return results[no_stairs]
    if no_stairs == 0:
        return 1
    if no_stairs < 0:
        return 0

    cur_total = 0
    for step in steps:
        result = climb_stairs(no_stairs - step)
        cur_total += result

    if no_stairs not in results:
        results[no_stairs] = cur_total
    return cur_total


def stairs_fibonacci(n):
    n += 1
    return int((1/math.sqrt(5)) * ((1 + math.sqrt(5))/2)**n - (1/math.sqrt(5)) * ((1 - math.sqrt(5))/2)**n)


def main():
    stairs = 50
    total = climb_stairs(stairs)
    print(f"Total combinations: {total:,}")
    print(f"Total combinations using fibonacci sequence: {stairs_fibonacci(50):,}")


if __name__ == "__main__":
    main()
