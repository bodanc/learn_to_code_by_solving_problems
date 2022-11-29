# number = 2
#
# while number < 100_000_000_000_000_000_000:
#     number = number ** 2
#     print(number)

# number = 4
#
# while number >= -1:
#     print(number)
#     number -= 1
#

# i = 0
#
# while i < 3:
#     j = 8
#     while j < 11:
#         print(i, j)
#         j += 1
#     i += 1

# x = 0
# y = 1
#
# while x < 3:
#     while y < 3:
#         print(x, y)
#         y += 1
#     x += 1

valid = False

while not valid:
    s = input()
    valid = len(s) == 5 and s[:2] == 'xy'
