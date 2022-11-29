
total_calories = 0

option_1 = int(input())
option_2 = int(input())
option_3 = int(input())
option_4 = int(input())

if option_1 == 1:
    total_calories += 461
elif option_1 == 2:
    total_calories += 431
elif option_1 == 3:
    total_calories += 420

if option_2 == 1:
    total_calories += 100
elif option_2 == 2:
    total_calories += 57
elif option_2 == 3:
    total_calories += 70

if option_3 == 1:
    total_calories += 130
elif option_3 == 2:
    total_calories += 160
elif option_3 == 3:
    total_calories += 118

if option_4 == 1:
    total_calories += 167
elif option_4 == 2:
    total_calories += 266
elif option_4 == 3:
    total_calories += 75

print('Your total calorie count is ' + str(total_calories) + '.')