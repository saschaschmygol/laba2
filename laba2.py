Ru_alfavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
En_alfavit = 'abcdefghijklmnopqrstuvwxyz'

while True:
    try:
        sdvig = int(input('Введите шаг сдвига '))
        break
    except ValueError:
        print('Водите число!!!!!!')


Flag = True
while Flag:
    mess = str(input('Введите сообщение для шифровки'))
    mess = mess.lower()
    for i in mess:
        if i not in Ru_alfavit and i not in En_alfavit:
            print('такого символа нет в алфавите, введите верное сообщение')
        else:
            Flag = False


lang = input('какой язык использовать? RU/EN')
slovo = ''

if lang == 'RU':
    for i in mess:
        mesto = Ru_alfavit.find(i)
        mesto2 = mesto + sdvig
        if mesto2 > 32:
            mesto2 -= 33
        simvol = Ru_alfavit[mesto2]
        slovo += simvol

else:
    for i in mess:
        mesto = En_alfavit.find(i)
        mesto2 = mesto + sdvig
        if mesto2 > 25:
            mesto2 -= 26
        simvol = En_alfavit[mesto2]
        slovo += simvol

print(slovo)



































































