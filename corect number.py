import random
num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def inter():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print("А может введете число от 1 до 100")
            
            
def compare():
    while True:
        s = inter()
        if s > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif s < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
compare()   







