
a_three = int(input())
a_two = int(input())
a_one = int(input())

b_three = int(input())
b_two = int(input())
b_one = int(input())

a_total = 3 * a_three + 2 * a_two + a_one
b_total = 3 * b_three + 2 * b_two + b_one

if a_total > b_total:
    print('a'.upper())
elif a_total < b_total:
    print('b'.upper())
else:
    print('t'.upper())
