"""
File: ClimbingStairs.py
Author: Truman Farr
tfarr@mail.sfsu.edu
trumanfarr@gmail.com
"""
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

https://leetcode.com/problems/climbing-stairs/
"""
import sys
import math

results = {}


def climb_stairs(no_stairs, steps=(1, 2)):
    """
        Given number of stairs, return total number of combinations possible with set step intervals.
        Parameters:
        ---------------
        no_stairs       Number of stairs to climb
        steps           (optional) List of possible step intervals to use
    """
    sys.setrecursionlimit(no_stairs + 250)  # Set recursion limit so Python doesn't cut method off early!
    steps = set(steps)  # Cast steps to set, to insure there are no duplicate values in steps
    assert len(steps) > 0  # Assert steps is not empty
    if no_stairs in results:  # Check if result of step number is already stored in results dict, if so, return value
        return results[no_stairs]
    if no_stairs == 0:  # Lowest possible case, only one possible combination available
        return 1
    if no_stairs < 0:  # Impossible scenario, overshot the end of the staircase, return 0
        return 0

    cur_total = 0  # Set cur_total (current total), to return after all step intervals are checked

    for step in steps:  # Iterate through step intervals
        result = climb_stairs(no_stairs - step)  # Check combination of staircase with one less step
        cur_total += result

    if no_stairs not in results:
        results[no_stairs] = cur_total  # If the result just calculated is NOT in the results dict, add it
    return cur_total


def stairs_fibonacci(no_stairs):
    """
        Using fibonacci sequence as an O(1) shortcut to described problem above.
        Parameters:
        ---------------
        no_stairs       Number of stairs to climb

        Note: There seems to be a discrepancy between climb_stairs() and stairs_fibonacci() when no_stairs is greater
        than ~100. I feel this may be due to max int length in Python, but more investigation needs to be done.
    """
    no_stairs += 1
    return int((1 / math.sqrt(5)) * ((1 + math.sqrt(5)) / 2) ** no_stairs - (1 / math.sqrt(5)) * (
            (1 - math.sqrt(5)) / 2) ** no_stairs)


def main():
    stairs = 100  # Change value to give results for different number of stairs
    print(f"Total combinations: {climb_stairs(stairs, [1, 2, 2]):,}")
    print(f"Total combinations using fibonacci sequence: {stairs_fibonacci(stairs):,}")


if __name__ == "__main__":
    main()
