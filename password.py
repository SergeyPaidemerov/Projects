import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '#$%&*+-=?@^_'
chars = ''
n = int(input('Введите количество паролей для генерации\n'))
lenght = int(input('Введите длину пароля\n'))
d = input('Включаются ли цифры 0123456789 в пароль (да\нет)?\n')
a = input('Включаются ли прописные (заглавные) буквы в пароль (да\нет)?\n').strip()
b = input('Включаются ли строчные буквы в пароль (да\нет)?\n').strip()
c = input('Включаются ли символы !#$%&*+-=?@^_? в пароль (да\нет)?\n').strip()
e = input('Исключать ли неоднозначные символы il1Lo0O (да\нет)?\n').strip()
if d.lower() == 'да':
    chars += digits
if a.lower() == 'да': 
    chars += uppercase_letters      
if b.lower() == 'да':
    chars += lowercase_letters
if c.lower() == 'да':
    chars += punctuation
if e.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
def generate_password(lenght, chars):
    password = ''
    for j in range(lenght):
        password += random.choice(chars)
    return password
for i in range(n):
    print(generate_password(lenght, chars))