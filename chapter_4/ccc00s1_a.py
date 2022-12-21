quarters = int(input())

machine_1 = int(input())
machine_2 = int(input())
machine_3 = int(input())

next_machine = 0
plays = 0

while quarters >= 1:

    quarters -= 1

    if next_machine == 0:
        machine_1 += 1
        if machine_1 == 35:
            machine_1 = 0
            quarters += 30
    elif next_machine == 1:
        machine_2 += 1
        if machine_2 == 100:
            machine_2 = 0
            quarters += 60
    elif next_machine == 2:
        machine_3 += 1
        if machine_3 == 10:
            machine_3 = 0
            quarters += 9

    plays += 1
    next_machine += 1

    if next_machine == 3:
        next_machine = 0

print('Martha plays', plays, 'times before going broke.')
