
# suplies = ['ручки', 'степлеры', 'карандаши', 'скоросшиватель']
# for i in range(len(suplies)):
    # print('Индекс', str(i), ':', suplies[i])
# sp = ['А', 'я', 'Я', 'а']
# sp.sort(key=str.lower)
# print(sp)
# print(id('spam'))


# def eggs(some_Parametr):
    # some_Parametr.append('Hello')
# spam = [1, 2 ,3]
# eggs(spam)
# print(spam)
# Учебный проект из книги "Автоматизация рутинных задач с помощью Python"
# def sp(spam):
   # if spam == ' ' or spam == '':
  #      print('Введите что-то')
  #  spam.insert(-1, 'и')    
  #  print(*spam)
# spr = input().split()
# sp(spr)

# stuff = {'веревка': 1, 'факел': 6, 'золотая монета': 42, 'кинжал': 1, 'стрела': 12}

# def displayInventory(inventory):
 #   print('Инвентарь:')
 #   item_total = 0
 #   for k, v in inventory.items():
  #      item_total += v
  #      print(' ', k, '-', v)
  #  print('Всего элементов:', str(item_total))
# displayInventory(stuff)

# print('Hello there!\n How are you?\n Im doing fine.')
# spam = 'Say hi to bob\'s mother'
# print(spam)
# from functools import reduce

# numbers = [1, 2, 3]
# result = reduce(lambda a, b: a * b, numbers, 10)
# print(result)

# validateInput
# while True:
  #  print('Укажите возраст')
  #  age = input()
  #  if age.isdecimal():
   #     break
  #  print('Введите число')
    
# while True:
  #  print('Выберите новый пароль (только буквы и цифры): ')
  #  password = input()
   # if password.isalnum():
   #     break
   # print('Пароли могут состоять только из букв и цифр.')
   
# def print_Picnic(items_Dict, left_Width, right_Width):
  #  print('Берем на пикник'.center(left_Width + right_Width, '-'))
  #  for k, v in items_Dict.items():
   #     print(k.ljust(left_Width, '.') + str(v).rjust(right_Width))
        
# picnic_Items = {'Сендвич': 4, 'яблоки': 12, 'чашки': 4, 'печенье':8000}
# print_Picnic(picnic_Items, 16, 5)
# print_Picnic(picnic_Items, 24, 7)

# модуль pyperclip
# import pyperclip
# pyperclip.copy('Hello world!')
# print(pyperclip.paste())

# myfile = open('myfile.txt', 'w')
# myfile.write('hello text file\n')
# myfile.write('goodbye text file\n')
# myfile.close()
# myfile = open('myfile.txt')
# print(myfile.readline())
# myfile = open('myfile.txt')
# print(myfile.read())
# print(open('myfile.txt').read())
# print('415-555-4242 - is this a phone number')
# print(is_Phone_number('415-555-4242'))
# d = {'a': 1, 'b': 2}
# import pickle
# with open('datafile.pkl', 'wb') as f:
  # pickle.dump(d, f)
 #  f.close()
# with open('datafile.pkl', 'rb') as file:
 #  e = pickle.load(file)
  # print(e)
# f = open('datafile.pkl', 'rb').read()
# print(f) - выводит байты
# name = dict(first='Bob', last='Smith')
# rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
# import json
# s = json.dumps(rec)
# o = json.loads(s)
# print(o == rec) - True
# heroRegex = re.compile(r'Бэтмен|Тина фей')
# mo1 = heroRegex.search('Бэтмен и Тина фей.')
# print(mo1.group())
# mo2 = heroRegex.search('Тина фей and Бэтмен.')
# print(mo2.group())
# batRegex = re.compile(r'Bat(man|car|copter|bat)')
# mo = batRegex.search('Batcar lost wheel')
# print(mo.group(1))
# print(os.name)
# print(os.environ) - environ({'ALLUSERSPROFILE': 'C:\\ProgramData'  сведения, которые касаются конфигурации компьютера, можно при помощи
# print(os.getenv('TMP')) При помощи функции getenv можно получить доступ к различным переменным среды.
# print(os.path.isfile("D:/Fortnite")) - False
# print(os.getcwd())
# print(os.path.isdir('D:/Fortnite')) - True
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('My hero - batman')
# mo2 = batRegex.search('My hero - Batwoman')
# print(mo2.group())
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('my number: 415-555-4242')
# print(mo1.group())
# mo2 = phoneRegex.search('My number: 555-4242')
# print(mo2.group()) - 555-4242
# os.mkdir(r"D:\folder") - Например, с помощью метода mkdir довольно легко создать папку, просто указав для нее желаемый путь.
# os.makedirs(r"D:\folder\first\second\third") - Благодаря функции makedirs можно создавать сразу несколько новых папок в неограниченном количестве, если предыдущая директория является родительской для следующей
# os.remove(r"D:\text.txt") - Избавиться от ненужного в дальнейшей работе файла можно с помощью метода remove
# os.rmdir(r"D:\folder") -  стереть из памяти папку, следует воспользоваться встроенной функцией rmdir
# os.removedirs(r"D:\folder\first\second\third") Для быстрого удаления множества пустых папок следует вызывать функцию removedirs
# os.startfile(r"D:\test.txt") Встроенные функции библиотеки os позволяют запускать отдельные файлы и папки прямиком из программы
# print(os.path.basename("D:/test.txt")) Преобразовать адрес объекта в название позволяет функция basename, которая содержится в подмодуле path из библиотеки os
# print(os.path.dirname("D:/folder/test.txt")) Обратная ситуация возникает тогда, когда пользователю нужно получить только путь к файлу, без самого названия объекта.
# import re
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('My hero - batman')
# mo3 = batRegex.search('My hero - Batwowowowowowowowman')
# print(mo3.group()) - Batwowowowowowowowman
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('My hero - batwoman')
# mo2 = batRegex.search('My hero - Batwowowowowowowowman')
# mo2.group() - Batwowowowowowowowman
# mo3 = batRegex.search('My hero - batman')
# print(mo3 == None) - True
s = 'Человек, план, канал: Панама'
newStr = ""  
for char in s:
  if char.isalnum():
    newStr += char.lower()
print(newStr)