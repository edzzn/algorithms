import sys


def solution(A):
    """Your solution goes here."""
    row_counter = 0
    max_height = 0
    for student_height in A:
        if student_height > max_height:
            max_height = student_height
            row_counter += 1
    return row_counter


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    # input = sys.stdin.readline().split()
    # A = [int(x) for x in input[0].split(",")]
    A = [5, 4, 3, 6, 1]
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    main()
