import sys


def solution(A):
    """Your solution goes here."""
    A.sort(reverse=True)
    diff = 0
    for item in A:
        if diff < 0:
            diff += item
        else:
            diff -= item
    return abs(diff)


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    # input = sys.stdin.readline().split()
    # A = [int(x) for x in input[0].split(",")]
    A = [1, 10, 2, 3, 4, 5]
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    main()
