pw_input = input()

valid_count = 0

lower_count = 0
upper_count = 0
digit_count = 0

for char in pw_input:
    if char.islower() or char.isupper() or char.isdigit():
        valid_count += 1
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1
    elif char.isdigit:
        digit_count += 1

if (len(pw_input) > 7 and len(pw_input) < 13
    and valid_count == len(pw_input)
    and lower_count > 2 and upper_count > 1 and digit_count > 0):
    print('Valid')
else:
    print('Invalid')
