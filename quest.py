print(' Приветствую вас в моем квесте,')
print(' Ваша задача не только сдать зачеты,')
print(' Но и развлечся')
print(' Нажмите 1 для старта')
qweewq = 0
chem = 0
phis = 0
pod = 0
health = 3
final = 0
geom = 0
russ = 0
finish = set('')
o0 = 1
a = input()
if a == '1':
    print(' Выберите 2 предмета на игру')
    print(' 1 - калькулятор')
    print(' 2 - суперподушка')
    print(' 3 - набор химика')
    print(' 4 - переводчик')
    print(' 5 - кофе')
    y1 = input()
    y2 = input()
    if y1 == '1' or y2 == '1':
        finish.add('Алгебру')
    if y1 == '5' or y2 == '5':
        health += 1
    if y1 == '4' or y2 == '4':
        finish.add('Английский ')
    if y1 == '2' or y2 == '2':
        pod = 1
    if y1 == '3' or y2 == '3':
        chem = 1
    print(' ПК или учеба')
    print(' 1 - ПК')
    print(' 2 - Учеба')
    a1 = input()
    if a1 == '1':
        print(' Выберите что вы будете делать?')
        print(' 1 - Играть')
        print(' 2 - Смотреть фильм')
        a2 = input()
        if a2 == '1':
            print(' 1 - VR')
            print(' 2 - PC GAME')
            a3 = input()
            if a3 == '1':
                x222 = 0
                x111 = 0
                print(' Вам нужно писать 1 или 2')
                print(' В зависимости от того что вы хотите выбрать')
                for i in range(5):
                    i1 = i % 2
                    if i == 0 or i1 == 0:
                        print('*** front / back ***')
                        x = input()
                        if x == '1':
                            x222 += 1
                    else:
                        print('*** right / left ***')
                        x = input()
                        if x == '2':
                            x111 += 1
                if x222 == 3:
                    if x111 == 2:
                        if y1 != '2' and y2 != '2':
                            print(' Вы вышли из сооружения и заснули, но')
                            print(' После вы проснулись в лучшем мире')
                            input()
                        else:
                            print(' Вы вышли из сооружения и заснули, но')
                            print(' Вы упали на суперподушку')
                            print(' Которая дала вам знаний,')
                            print(' С помощью нее вы все сдали на 5')
                            input()
                        qweewq = 1
                if x222 == 0 and x111 == 0 or x111 == 1:
                    print('Вам доступен супер учебник по геометрии')
                    geom = 1
                if x222 == 0 and x111 == 2:
                    print('Вам доступен супер учебник по русскому')
                    russ = 1
                if qweewq == 0:
                    print('Что будете делать дальше')
                    print(' 1 - пойду спать')
                    print(' 2 - пойду учить уроки')
                    a4 = input()
                    if a4 == '1':
                        final = 1
                    if a4 == '2':
                        o0 = 1
            elif a3 == '2':
                print(' Выберите игру')
                print(' 1 - CS2')
                print(' 2 - Fortnite')
                print(' 3 - GTA V')
                a4 = input()
                if a4 == '1' or a4 == '2':
                    print(' Вы поиграли 2 часа')
                    if a4 == '1' and y1 != 4 and y2 != 4:
                        print(' Вы получили навык английского языка')
                        finish.add('Английский ')
                    print(' 1 - пойти спать')
                    print(' 2 - пойти играть дальше')
                    print(' 3 - пойти учить уроки')
                    a5 = input()
                    if a5 == '1':
                        final = 1
                    elif a5 == '2':
                        print(' Вы уснули и проспали экзамен')
                        input()
                    elif a5 == '3':
                        o0 = 1
                elif a4 == '3':
                    print('!!!!! Вы стали жестоким и не пошли')
                    print('!!!!! Сдавать зачеты')
                    input()
        elif a2 == '2':
            print(' ФИЛЬМ / СЕРИАЛ ')
            a3 = input()
            if a3 == '1':
                print(' Выберите фильм:')
                print(' 1 - Социальная сеть')
                print(' 2 - БОБРЫ-ЗОМБИ')
                print(' 3 - Властелин колец')
                a4 = input()
                if a4 == '1':
                    print(' Вам доступен новый код')
                    finish.add('Информаттику ')
                elif a4 == '2':
                    print(' Тебе выдан штраф')
                    print(' За этот ответ')
                    finish = set('')
                elif a4 == '3':
                    print(' Вы заснули и проспали')
                    input()
                if a4 == '1' or a4 == '2':
                    print(' Пойти спать / делать уроки')
                    a5 = input()
                    if a5 == '1':
                        final = 1
                    elif a5 == '2':
                        o0 = 1
            elif a3 == '2':
                print(' Выберите сериал')
                print(' 1 - Breaking Bad')
                print(' 2 - Теория большого взрыва')
                print(' 3 - Слово пацана')
                a4 = input()
                if a4 == '1':
                    if chem == 1:
                        print(' Вы улучшили свои навыки в химии')
                        chem += 1
                    else:
                        print(' Вы улучшили свои навыки в химии')
                        chem = 1
                elif a4 == '2':
                    print(' Вы улучшили свои навыки в физике')
                    phis = 1
                elif a4 == '3':
                    print(' Ну это просто...')
                    input()
    if a1 == '2' or o0 == 1:
        while health != 0:
            a2 = input()
            print(' 1 - Математика')
            print(' 2 - Языки')
            print(' 3 - Остальное')
            if a2 == '1':
                a3 = input()
                print(' 1 - Геометрия')
                print(' 2 - Алгебра')
                print(' 3 - Информатика')
                if a3 == '1':
                    if geom == '1':
                        finish.add('Геометрию ')
                    else:
                        print(' Катит это ...')
                        print('1 - Сторона прилегающая к прямому углу')
                        print('2 - Сторона лежащая против прямого угла')
                        print('3 - Катет - сторона прилегающая к прямому углу')
                        a4 = input()
                        if a4 == '1':
                            finish.add('Геометрию ')
                            print(' Вы выучили геометрию')
                        elif a4 == '2':
                            print('Гений')
                            input()
                        elif a4 == '3':
                            finish.add('Геометрию')
                            finish.add('Русский ')
                            print('Вы выучили геометрию и русский')
                            health -= 1
                elif a3 == '2':
                    if y1 == '1' or y2 == '1':
                        print('  Вы просто так потратили энергию')
                        health -= 1
                    else:
                        print(' √1936 = ...')
