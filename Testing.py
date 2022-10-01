word = input("Введите строку")
i = len(word) - 1
message = ''
while i >= 0:
    message = message + word[i]
    i = i - 1

print ("Перевернутая строка: "+ message)