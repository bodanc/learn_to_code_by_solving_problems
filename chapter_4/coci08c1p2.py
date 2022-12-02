pattern_A = 'ABC'
pattern_B = 'BABC'
pattern_C = 'CCAABB'

points_A = 0
points_B = 0
points_C = 0

i = 0

nb_questions = int(input())
answers = input()

while i < nb_questions:
    if answers[i] == pattern_A[i % len(pattern_A)]:
        points_A += 1
    if answers[i] == pattern_B[i % len(pattern_B)]:
        points_B += 1
    if answers[i] == pattern_C[i % len(pattern_C)]:
        points_C += 1
    i += 1

most = points_A
if points_B > most:
    most = points_B
if points_C > most:
    most = points_C

print(most)

if points_A == most:
    print('Adrian')
if points_B == most:
    print('Bruno')
if points_C == most:
    print('Goran')
