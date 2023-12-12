string = (input('Введите текст: '))
c = input('Введите слово которое хотите заменить: ')
b = input('Введите слово на которое хотите заменить: ')
word = []
pos = -1
last_pos = -1

while ' ' in string[pos + 1:]:
    pos = string.index(' ', pos + 1)
    word.append(string[last_pos + 1:pos])
    last_pos = pos

word.append(string[last_pos + 1:])
print(word)
for a in range (len(word)):
    if word[a] == c:
        word[a] = b
print(word)