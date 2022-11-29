line = input()

count_positive = line.count(':-)')
count_negative = line.count(':-(')

if (count_positive == 0 and count_negative == 0):
    print('none')
elif (count_positive > count_negative):
    print('happy')
elif (count_positive < count_negative):
    print('sad')
else:
    print('unsure')
