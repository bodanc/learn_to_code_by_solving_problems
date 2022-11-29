target_population = int(input())

total = int(input())
daily = int(input())

previous_day = total

day = 0

while total <= target_population:

    total += (daily * previous_day)
    previous_day = previous_day * daily

    day += 1

print(f'{day}')
