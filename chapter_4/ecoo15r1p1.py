for dataset in range(10):
    nb_blue = 0
    nb_brown = 0
    nb_green = 0
    nb_orange = 0
    nb_pink = 0
    nb_red = 0
    nb_violet = 0
    nb_yellow = 0

    done = False

    while not done:
        line = str(input())

        if line == 'end of box':
            done = True
        elif line == 'blue':
            nb_blue += 1
        elif line == 'brown':
            nb_brown += 1
        elif line == 'green':
            nb_green += 1
        elif line == 'orange':
            nb_orange += 1
        elif line == 'pink':
            nb_pink += 1
        elif line == 'red':
            nb_red += 1
        elif line == 'violet':
            nb_violet += 1
        elif line == 'yellow':
            nb_yellow += 1

    nb_handfuls = ((nb_blue + 6) // 7 + (nb_brown + 6) // 7 + (nb_green + 6) // 7 +
                   (nb_orange + 6) // 7 + (nb_pink + 6) // 7 + (nb_violet + 6) // 7 +
                   (nb_yellow + 6) // 7)

    print(nb_handfuls * 13 + nb_red * 16)
