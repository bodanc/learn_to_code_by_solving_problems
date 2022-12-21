nb_lines = int(input())

for dataset in range(nb_lines):
    line = str(input())

    result = ''
    total = 1

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            total += + 1
        else:
            result += f'{total} {line[i]} '
            total = 1

    result += f'{total} {line[-1]}'

    print(result)
