nb_lines = int(input())

for dataset in range(nb_lines):
    line = str(input())

    i = 0
    result = ''

    while i < len(line):
        total = 1
        while i < len(line) - 1 and line[i] == line[i + 1]:
            i += 1
            total += 1
        result += f'{total} {line[i]} '
        i += 1

    print(result.strip())
