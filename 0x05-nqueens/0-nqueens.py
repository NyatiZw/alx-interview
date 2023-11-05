#!/usr/bin/python3
"""
    The N queens puzzel
"""

import sys


def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    def backtrack(row):
        if row == N:
            results.append(board[:])
        else:
            for col in range(N):
                if is_valid(board, row, col):
                    board.append(col)
                    backtrack(row + 1)
                    board.pop()

    board = []
    results = []

    backtrack(0)

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        formatted_solution = [[i, c] for i, c in enumerate(solution)]
        print(formatted_solution)


if __name__ == "__main__":
    main()
