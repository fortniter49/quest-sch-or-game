a = input()
#y1 - калькулятор
#y2 - подушка
#y3 - набор химика
#y4 - переводчик
#y5 - кофе
if a == '1': 
    a1 = input()
    if a1 == '1': #PC
        a2 = input()
        if a2 == '1':  #GAME
            a3 = input()
            if a3 == '1':  #VR
                x222 = 0
                x111 = 0
                for i in range(5):
                    i1 = i % 2
                    if i == 0 or i1 == 0:
                        print('front / back')
                        x = input()
                        if x == '1':
                            x222 += 1
                    else:
                        print('right / left')
                        x = input()
                        if x == '2':
                            x111 += 1
                if x222 == 3:
                    if x111 == 2:
                        print('lose')
                elif x222 == 0 and x111 == 0 or x111 == 1:
                    print ('вам доступен супер учебник по геометрии')
                    geom = 1
                elif x222 == 0 and x111 == 2:
                    print('вам доступен супер учебник по русскому')
                    russ = 1
