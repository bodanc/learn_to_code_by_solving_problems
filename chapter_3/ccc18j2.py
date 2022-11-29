parking_spaces = int(input())

yesterday = input()
today = input()

occupied = 0

for index in range(len(yesterday)):
    if yesterday[index] == 'C' and today[index] == 'C':
        occupied += 1

print(occupied)
