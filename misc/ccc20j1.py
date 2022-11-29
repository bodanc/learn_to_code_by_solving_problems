s = int(input())
m = int(input())
l = int(input())

happiness_index = 1 * s + 2 * m + 3 * l

if happiness_index >= 10:
    print(f'happy')
else:
    print(f'sad')
