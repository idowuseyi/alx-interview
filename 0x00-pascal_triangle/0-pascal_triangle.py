#!/usr/bin/python3
'''Function that prints pascals triangle with the height as input.'''


def pascal_triangle(n):
    '''Function that return a pascal triangle'''
    check_result = []
    if type(n) is not int or n <= 0:
        return check_result
    result = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        row.append(1)
        result.append(row)
    return result