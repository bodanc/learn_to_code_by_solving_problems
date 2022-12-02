sentence = input()

i = 0
result = ''

while i < len(sentence):
    result += sentence[i]

    if sentence[i] in 'aeiou':
        i += 3
    else:
        i += 1

print(result)
