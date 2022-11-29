
nb_questions = int(input())

answers_student = ''

for _ in range(nb_questions):
    answers_student += input()

answers_key = ''

for _ in range(nb_questions):
    answers_key += input()

correct_answers = 0

for i in range(nb_questions):
    if answers_student[i] == answers_key[i]:
        correct_answers += 1

print(correct_answers)
