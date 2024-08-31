# catNames = []
# while True:
    # print('Укажите имя кота или кошки', str(len(catNames) + 1) + ' (<Enter> для завершения) : ')
    # name = input()
    # if name == '' or name == ' ':
        # break
     # elif name == 'Enter' or name == 'enter':
     #   break
   # catNames = catNames + [name]
# print('Имена котов и кошек:')
# for name in catNames:
   # print('  ' + name)
   
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

# gird = [['.', '.', '.', '.', '.', '.'],
    #    ['.', 'O', 'O', '.', '.', '.'],
     #   ['O', 'O', 'O', 'O', '.', '.'],
     #   ['O', 'O', 'O', 'O', 'O', '.'],
     #   ['.', 'O', 'O', 'O', 'O', 'O'],
     #   ['O', 'O', 'O', 'O', 'O', '.'],
     #   ['.', '.', '.', '.', '.', '.'],
     #   ['.', 'O', 'O', '.', '.', '.'],
    #    ['O', 'O', 'O', 'O', '.', '.'],
     #   ['.', '.', '.', '.', '.', '.'],]
# for i in gird:
   # for j in gird:
    #    print(gird[0][0], gird[1][0], gird[2][0], gird[3][0], gird[4][0], gird[5][0], gird[6][0], gird[7][0], gird[8][0], end='')
    #    print(gird[0][1], gird[1][1], gird[2][1], gird[3][1], gird[4][1], gird[5][1], gird[6][1], gird[7][1], gird[8][1], end='')
   #     print(gird[0][2], gird[1][2], gird[2][2], gird[3][2], gird[4][2], gird[5][2], gird[6][2], gird[7][2], gird[8][2], end='')
    #    print(gird[0][3], gird[1][3], gird[2][3], gird[3][3], gird[4][3], gird[5][3], gird[6][3], gird[7][3], gird[8][3], end='')
   #     print(gird[0][4], gird[1][4], gird[2][4], gird[3][4], gird[4][4], gird[5][4], gird[6][4], gird[7][4], gird[8][4], end='')
    #    print(gird[0][5], gird[1][5], gird[2][5], gird[3][5], gird[4][5], gird[5][5], gird[6][5], gird[7][5], gird[8][5], end='')
    
# игра крестики нолики из книги автоматизация рутинных задач с помощью python
 # the_Board = {'top-L': '', 'top-M': '', 'top-R': '',
         #    'mid-L': '', 'mid-M': '', 'mid-R': '',
         #    'low-L': '', 'low-M': '', 'low-R': ''}
#def printBoard(board):
   # print(board['top-L'] + '|' + board['top-M'] + '|' + \
  #        board['top-R'])
  #  print('-+-+-')
  #  print(board['mid-L'] + '|' + board['mid-M'] + '|' + \
  #        board['mid-R'])
 #   print('-+-+-')
   # print(board['low-L'] + '|' + board['low-M'] + '|' + \
   #       board['low-R'])
# turn = 'X'
# for i in range(9):
  #  printBoard(the_Board)
  #  print('Ход для', turn, 'куда ходить')
  #  move = input()
   # the_Board[move] = turn
   # if turn == 'X':
    #    turn = 'O'
   # else:
    #    tunr = 'X'
 # printBoard(the_Board)

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

# print(ord('A'))  - 65
# print(ord('4')) - 52
# print(ord('!')) - 33
# print(chr(65)) - 'A'
# print(ord('A') < ord('B')) - True
# print(chr(ord('s'))) - s
# print(chr(ord('a') + 1)) - b

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

# isPhoneNumber
# def is_Phone_number(text):
   # if len(text) != 12:
    #    return False
   # for i in range(0, 3):
   #     if not text[i].isdecimal():
   #         return False
    #if text[7] != '-':
    #    return False
   # for i in range(8, 12):
   #     if not text[i].isdecimal():
    #        return False
    #return True
# print('415-555-4242 - is this a phone number')
# print(is_Phone_number('415-555-4242'))
from zipfile import ZipFile
import json
with ZipFile('data.zip') as zip_file:
    players = []
    for file in zip_file.namelist():
        if file.split('.')[-1] == 'json':
            try:
                with zip_file.open(file) as json_file:
                    player = json.load( json_file)
                    if player['team'] == 'Arsenal':
                        players.append(f'{player['first_name']} {player['last_name']}')
            except:
                pass
print(*sorted(players), sep='\n')