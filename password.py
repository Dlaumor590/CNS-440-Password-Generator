from random import choice
from random import randint
from random import shuffle


caractères = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&_-'
chiffres = '0123456789'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '!@#$%&_-'
password = ''
pass_min_len = 10
pass_max_len = 34
pass_len = int(input('****Votre mot de passe doit contenir au moins 10 caractères et au plus 34 caractères****\nCombien de caractères souhaitez-vous pour votre mot de passe ? : '))
while pass_len < 10:
    print('!!!Désolé votre mot de passe doit contenir au moins 10 caractères')
    pass_len = int(input(
        '****Votre mot de passe doit contenir au moins 10 caractères et au plus 34 caractères****\nComien de caractères souhaitez-vous pour votre mot de passe ? : '))
while pass_len > 34:
    print('!!!Désolé votre mot de passe ne doit pas dépasser 34 caractères')
    pass_len = int(input(
        '****Votre mot de passe doit contenir au moins 10 caractères et au plus 34 caractères****\nComien de caractères souhaitez-vous pour votre mot de passe ? : '))
for i in range(randint(1, 2)):
    password += choice(upper)
for i in range(randint(1, 2)):
    password += choice(lower)
for i in range(randint(1, 2)):
    password += choice(chiffres)
for i in range(randint(1, 2)):
    password += choice(symbol)
pass_len1 = len(password)
if len(password) < 10:
    for i in range(pass_len1, pass_len):
        password += choice(caractères)
if 'a' in password:
    password = password.replace('a', '@')
if 'e' in password:
    password = password.replace('e', '3')
if 's' in password:
    password = password.replace('s', '$')
if 'o' in password:
    password = password.replace('o', '0')

password1 = password.split()
shuffle(password1)
password.join(password1)
print('Voici votre mot de passe sécurisé:', password)
