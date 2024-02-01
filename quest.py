a = input()
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
                print(' Вам нужно писать 1 или 2 в зависимости от того что вы хотите выбрать')
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
                    print ('вам доступен супер учебник по геометрии')
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
            elif a3 == '2':  #PCGAME
                a4 = input()
                if a4 == '1' or a4 == '2':  #CSFORT
                    a5 = input()
                    if a5 == '1':
                        print('end')  #END
                    elif a5 == '2':
                        o0 = 1
                elif a4 == '3':
                    a5 = input()
                    if a5 == '1':
                        print('end')  #END
                    elif a5 == '2':
                        o0 == 1
        elif a2 == '2':  #FILM
            a3 = input()
            if a3 == '1':  #FILM
                a4 = input()
                if a4 == '1':
                    print('доступен код')
                    kod = 1
                elif a4 == '2':
                    print('вы потеряли ...')
                    y2 = 0
                elif a4 == '3':
                    print('сон')  #END
                if a4 == '1' or a4 == '2':
                    a5 = input()
                    if a5 == '1':
                        print(end)  #END
                    else:
                        o0 == 1
            elif a3 == '2':
                print('')#series
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
