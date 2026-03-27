
stack = []
word = input("Введіть слово: ")

for letter in word:
    stack.append(letter)

reversed_word = ""

while len(stack) > 0:
    reversed_word += stack.pop()
print("----------------------------------")
print("Перевернуте слово:", reversed_word)