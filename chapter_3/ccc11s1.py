nb_lines = int(input())

tT_english = 0
sS_french = 0


for _ in range(nb_lines):
    line = input()
    for char in line:
        if (char == 't') or (char == 'T'):
            tT_english += 1
        elif (char == 's') or (char == 'S'):
            sS_french += 1


if tT_english > sS_french:
    print('English')
elif tT_english < sS_french:
    print('French')
else:
    print('French')
