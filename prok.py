otvet = 0
vsego = 5

b = 'Your name: '
print(b)
name = input()


# Считываем вопрос
with open('D:\python\proekt\example.txt', 'r') as f:
   question_text = f.readline()
   variants_count = int(f.readline())
   right_variant = int(f.readline())
   variants = []
   for i in range(variants_count):
      variants.append(f.readline())

# Задаем вопрос
print('Вопрос номер 1')
print(question_text)
for variant in variants:
   print(variant)
selected_variant = int(input('Введи номер варианта, который кажется вам правильным:'))
if selected_variant == right_variant:
   print('Вы ответили на вопрос правильно')
   otvet = otvet + 1
else:
   print('Неправильный ответ')

   

with open('D:\python\proekt\example2.txt', 'r') as f:
   question_text = f.readline()
   variants_count = int(f.readline())
   right_variant = int(f.readline())
   variants = []
   for i in range(variants_count):
      variants.append(f.readline())

# Задаем вопрос
print('Вопрос номер 2')
print(question_text)
for variant in variants:
   print(variant)
selected_variant2 = int(input('Введи номер варианта, который кажется вам правильным:'))
if selected_variant2 == right_variant:
   print('Вы ответили на вопрос правильно')
   otvet = otvet + 1
else:
   print('Неправильный ответ')


with open('D:\python\proekt\example3.txt', 'r') as f:
   question_text = f.readline()
   variants_count = int(f.readline())
   right_variant = int(f.readline())
   variants = []
   for i in range(variants_count):
      variants.append(f.readline())

# Задаем вопрос
print('Вопрос номер 3')
print(question_text)
for variant in variants:
   print(variant)
selected_variant3 = int(input('Введи номер варианта, который кажется вам правильным:'))
if selected_variant3 == right_variant:
   print('Вы ответили на вопрос правильно')
   otvet = otvet + 1
else:
   print('Неправильный ответ')


with open('D:\python\proekt\example4.txt', 'r') as f:
   question_text = f.readline()
   variants_count = int(f.readline())
   right_variant = int(f.readline())
   variants = []
   for i in range(variants_count):
      variants.append(f.readline())

# Задаем вопрос
print('Вопрос номер 4')
print(question_text)
for variant in variants:
   print(variant)
selected_variant4 = int(input('Введи номер варианта, который кажется вам правильным:'))
if selected_variant4 == right_variant:
   print('Вы ответили на вопрос правильно')
   otvet = otvet + 1
else:
   print('Неправильный ответ')



with open('D:\python\proekt\example5.txt', 'r') as f:
   question_text = f.readline()
   variants_count = int(f.readline())
   right_variant = int(f.readline())
   variants = []
   for i in range(variants_count):
      variants.append(f.readline())

# Задаем вопрос
print('Вопрос номер 5')
print(question_text)
for variant in variants:
   print(variant)
selected_variant5 = int(input('Введи номер варианта, который кажется вам правильным:'))
if selected_variant5 == right_variant:
   print('Вы ответили на вопрос правильно')
   otvet = otvet + 1
else:
   print('Неправильный ответ')

print (otvet, 'верных ответов из' , vsego)

with open('D:\python\proekt\ouput.txt', 'w') as file:
    file.write('Name:')
    file.write(str(name))
    file.write(' |' )
    file.write(str(otvet))
    file.write(' правильных ответов из ')
    file.write(str(vsego))
    file.write(' | ')
    file.write('Ответы ')
    file.write('пользователя ')
    file.write(str(name))
    file.write(': ')
    file.write(str(selected_variant))
    file.write(',')
    file.write(str(selected_variant2))
    file.write(',')
    file.write(str(selected_variant3))
    file.write(',')
    file.write(str(selected_variant4))
    file.write(',')
    file.write(str(selected_variant5))
    file.write(' | ')
    file.write('Правильные ответы: ')
    file.write('3,4,2,1,4')
