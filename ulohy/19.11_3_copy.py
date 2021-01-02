import random

with open('text.19.11_3.txt', 'r') as file:
    text = [line.strip().split() for line in file.readlines()]

for line in text:
    for word in line:
        print(word, end = ' ')
    print('\n', end='')
print('\n')

new_text = []

for line in text:
    for word in line:
        word = list(word)
        # start, end = word[0], word[len(word)-1]
        # word.remove(start)
        # word.remove(end)
        # random.shuffle(word)
        # word = ''.join(word)
        # word = start + word + end + " "
        mixer = word[1:-1]
        random.shuffle(mixer)
        word = word[0] + ''.join(mixer) + word [-1] + " "
        new_text.append(word)
    new_text.append("\n")

for line in new_text:
    print(line, end = '')

with open('poprehadzovany_text.txt', 'w') as file:
    for line in new_text:
        file.write(line)
