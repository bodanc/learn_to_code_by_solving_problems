ticket_number = int(input())

late_students = 0
students_in_line = 0

line = ''

while line != 'EOF':
    line = input()
    if line == 'TAKE':
        ticket_number += 1
        late_students += 1
        students_in_line += 1
        if ticket_number > 999:
            ticket_number = 1
    elif line == 'SERVE':
        students_in_line -= 1
    elif line == 'CLOSE':
        print(late_students, students_in_line, ticket_number)
        late_students = 0
        students_in_line = 0
