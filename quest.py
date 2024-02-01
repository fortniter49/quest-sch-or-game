print(' приветствую вас в моем квесте,')
print(' ваша задача не только сдать зачеты,')
print(' но и развлечся')
print(' нажмите 1 для старта')
a = input()
if a = '1':
    print(' Выберите 2 предмета на игру')
    print(' 1 - калькулятор')
    print(' 2 - суперподушка')
    print(' 3 - набор химика')
    print(' 4 - переводчик')
    print(' 5 - кофе')
    y1 = input()
    y2 = input()
    if a == '1':
        print(' ПК или учеба')
        print(' 1 - ПК')
        print(' 2 - учеба')
        a1 = input()
        if a1 == '1':
            print(' Выберите что вы будете делать?')
            print(' 1 - играть')
            print(' 2 - смотреть фильм')
            a2 = input()
            if a2 == '1':
                print(' 1 - VR')
                print(' PC GAME')
                a3 = input()
                if a3 == '1':
                    x222 = 0
                    x111 = 0
                    print(' Вам нужно писать 1 или 2')
                    print(' в зависимости от того что вы хотите выбрать')
                    for i in range(5):
                        i1 = i % 2
                        if i == 0 or i1 == 0:
                            print('*** front / back*** ')
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
                                print('!!!!! Вы вышли из сооружения и заснули, но')
                                print('!!!!! после вы проснулись в лучшем мире')
                                print('END END END END END END')
                            else:
                                print('!!!!! Вы вышли из сооружения и заснули, но')
                                print('!!!!! вы упали на суперподушку которая дала вам знаний,')
                                print('!!!!! с помощью нее вы все сдали на 5')
                                print('END END END END END END')
                    if x222 == 0 and x111 == 0 or x111 == 1:
                        print('вам доступен супер учебник по геометрии')
                        geom = 1
                    if x222 == 0 and x111 == 2:
                        print('вам доступен супер учебник по русскому')
                        russ = 1
                    print('Что будете делать дальше')
                    print(' 1 - пойду спать')
                    print(' 2 - пойду учить уроки')
                    a4 = input()
                    if a4 == '1':
                        print('!!!!! Вы пошли поспать, но когда проснулись')
                        print('!!!!! подумали что вы в VR и долго пытались')
                        print('!!!!! понять на какую кнопку встать с кровати')
                        print('!!!!! в итоге вы опздали на экзамены')
                        print('END END END END END END')
                    elif a4 == '2':
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
                            eng = 1
                        print(' 1 - пойти спать')
                        print(' 2 - пойти играть дальше')
                        print(' 3 - пойти учить уроки')
                        a5 = input()
                        if a5 == 1:
                            if y1 == 1 or y2 == 1:
                                print(' Вы сдали хорошо')
                                print(' только алгебру, из-за калькулятора')
                                print(' остальное вы сдали на 3')
                                print('END END END END END END')
                            else:
                                print(' Вы сдали все на 3')
                                print('END END END END END END')
                    elif a4 == '3':
                        print('!!!!! Вы стали жестоким и не пошли')
                        print('!!!!! сдавать зачеты')
                        print('END END END END END END')
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
                        kod = 1
                    elif a4 == '2':
                        print(' Тебе выдан штраф')
                        print(' за этот ответ')
                        y1 = 0
                        y2 = 0
                        eng = 0
                        russ = 0
                        geom = 0
                    elif a4 == '3':
                        print(' Вы заснули и проспали')
                        print('END END END END END END')
                    if a4 == '1' or a4 == '2':
                        print(' Пойти спать / делать уроки')
                        a5 = input()
                        if a5 == '1':
                            if kod == 1:
                                if y1 == 1 or y2 == 1:
                                    print(' Вы сдали алгебру и информатику')
                                    print(' на 5, остальное на 3')
                                    print('END END END END END END')
                                else:
                                    print(' Вы сдали информатику на 5,')
                                    print(' остальное на 3')
                                    print('END END END END END END')
                            elif y1 == 1 or y2 == 1:
                                print(' Вы сдали математику на 5,')
                                print(' остальное на 3')
                                print('END END END END END END')
                            else:
                                print(' Вы сдали все предметы на 3')
                                print('END END END END END END')
                        else:
                            o0 == 1
                elif a3 == '2':
                    print(' Выберите сериал')
                    print(' 1 - Breaking Bad')
                    print(' 2 - Теория большого взрыва')
                    print(' 3 - Слово пацана')
                    a4 = input()
                    if a4 == 1:
                        if y1 == 3 or y2 == 3:
                            print(' Вы улучшили свои навыки в химии')
                            chem = 2
                        else:
                            print(' Вы улучшили свои навыки в химии')
                            chem = 1
                    elif a4 == 2:
                        print(' Вы улучшили свои навыки в физике')
                        phis = 1
                    elif a4 == 3:
                        print(' Ну это просто...')
                        print('END END END END END END')
        if a1 == '2' or o0 == 1:
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
                    if geom == 1:
                        print(' У вас есть супер учебник по геометрии,')
                        print(' вы полностью выучили геометрию')
                        b1 = 1
                    else:
                        print('Вы выучили геометрию')
                    print(' 1 - пойти спать')
                    print(' 2 - продолжить учить уроки')
                    a4 = input()
                    if a4 == 1:
                        print('b')
