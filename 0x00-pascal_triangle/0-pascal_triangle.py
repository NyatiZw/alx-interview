#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    returns list of lists of integer representing 
    Pascal's triangle of n
    """
    if int(n) <= 0:
        return []
    else:
        n += 1


if __name__ == "__main__":
    main()
