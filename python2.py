stack = []
word = input("Введіть слово: ")

# лічильник букв
count = 0

for letter in word:
    stack.append(letter)
    count += 1   # рахуємо букви

reversed_word = ""

while len(stack) > 0:
    reversed_word += stack.pop()

print("----------------------------------")
print("Перевернуте слово:", reversed_word)
print("Кількість букв:", count)
