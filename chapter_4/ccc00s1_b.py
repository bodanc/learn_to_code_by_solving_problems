quarters = int(input())

machine_1 = int(input())
machine_2 = int(input())
machine_3 = int(input())

plays = 0

while quarters > 0:

    quarters -= 1
    machine = plays % 3

    if machine == 0:
        machine_1 += 1
        if machine_1 % 35 == 0:
            quarters += 30
    elif machine == 1:
        machine_2 += 1
        if machine_2 % 100 == 0:
            quarters += 60
    elif machine == 2:
        machine_3 += 1
        if machine_3 % 10 == 0:
            quarters += 9

    plays += 1

print(f'Martha plays {plays} times before going broke.')
