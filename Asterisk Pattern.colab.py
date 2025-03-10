# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mXOMnac5uNeT0rlKuhzNqTHrtIj3k07e
"""

# Create Right-Angled Triangle
# *
# **
# ***
# ****
N = int(input())

for i in range(1, N + 1):
    print("*" * i)

# Create an Inverted Triangle
# *****
# ****
# ***
# **
# *
N = int(input())
for i in range(N, 0, -1):
    print("*" * i)

# Create Half-Diamond Shape
# *
# **
# ***
# **
# *
N = int(input())
for i in range(1, N + 1):
    print("*" * i)
for i in range(N - 1, 0, -1):
    print("*" * i)

N = int(input())
for i in range(N, 0, -1):
    print("*" * i)
for i in range(2, N + 1):
    print("*" * i)

# Create a Pyramid
#      *
#     ***
#    *****
#   *******
N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# Create a Diamond Shape
#      *
#     ***
#    *****
#     ***
#      *
N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i -1))
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# Create a Hollow-Diamond Shape
#    *
#  *   *
# *     *
#  *   *
#    *
N = int(input())
for i in range(1, N + 1):
    if i == 1:
        print(' ' * (N - i) + '*')
    else:
        print(' ' * (N - i) + '*' + ' ' * (2 * i - 3) + '*')
for i in range(N - 1, 0, -1):
    if i == 1:
        print(' ' * (N- i) + '*')
    else:
        print(' ' * (N - i) + '*' + ' ' * (2 * i - 3) + '*')

# Create a Hollow Diamond in Hollow Rectangle

N = int(input())
center = (N - 1) / 2  # Handles both even and odd N
for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1:
            print('*', end='')
        elif abs(i - center) + abs(j - center) == N // 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# Create a Hollow-Diamond shape inside a rectangle
N = int(input())
for i in range(N, 0, -1):
    if i == N:     # Adding an extra asterisk in the first line.
        print("*" * (i + 1), end="")
    else:
        print("*" * i, end=" ")
    print(" " * (N - i) * 2, end="")
    print("*" * i)
for i in range(2, N + 1):
    if i == N:    # Adding an extra asterisk in the last line.
        print("*" * (i + 1), end="")
    else:
        print("*" * i, end=" ")
    print(" " * (N - i) * 2, end="")
    print("*" * i)



N = int(input())
for i in range(N, 0, -1):
    print("*" * i, end="")
    print(" " * (N - i) * 2, end="")
    print("*" * i)
for i in range(2, N + 1):
    print("*" * i, end="")
    print(" " * (N - i) * 2, end="")
    print("*" * i)

# Create a Rectangle/Square
N = int(input("N: "))
M = int(input("M: "))

for i in range(N):
    for j in range(M):
        print("*", end="")
    print()

# Create a Square
N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 or i == N or j == 1 or j == N:
            print("*", end=" ")
        else:
            print("*", end=" ")
    print()

# Create a Hollow-Square
# * * * * *
# *       *
# *       *
# *       *
# *       *
# * * * * *

N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 or i == N or j == 1 or j == N:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Create pattern like
# ******
# *    *
# *    *
# ******
N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 or i == N or j == 1 or j == N:
            print("*", end="")
        else:
            print(" ", end="")
    print()