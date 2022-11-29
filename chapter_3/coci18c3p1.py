str = input()

match_index = 0
match = ''
total = 0

for char in str:
    if match_index == 0:
        match = 'H'
    elif match_index == 1:
        match = 'O'
    elif match_index == 2:
        match = 'N'
    else:
        match = 'I'
    if char == match:
        match_index += 1
        if match_index == 4:
            match_index = 0
            total = total + 1

print(total)
