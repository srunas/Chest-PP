import logging

logging.basicConfig(filename="Info.log", level=logging.DEBUG, format ="%(asctime)s %(levelname)s %(message)s" )


print("Программа Шахматы.")
logging.info("Начался ввод координат k,l,m,n")
while True:
    try:
        k = int(input("Введите первую координату первой фигуры: "))
        if k > 8 or k < 1:
            logging.error("Ошибка некорректного ввода")
            print("Вы ввели неверную координату")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Вы ввели не верное значение")
        pass

while True:
    try:
        l = int(input("Введите  вторую координату первой фигуры: "))
        if l > 8 or l < 1:
            logging.error("Ошибка некорректного ввода")
            print("Вы ввели неверную координату")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Вы ввели не верное значение")
        pass

while True:
    try:
        m = int(input("Введите первую координату второй фигуры: "))
        if m > 8 or m < 1:
            logging.error("Ошибка некорректного ввода")
            print("Вы ввели неверную координату")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Вы ввели не верное значение")
        pass

while True:
    try:
        n = int(input("Введите вторую координату второй фигуры: "))
        if n > 8 or n < 1:
            logging.error("Ошибка некорректного ввода")
            print("Вы ввели неверную координату")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Вы ввели не верное значение")
        pass

logging.info("Началась проверка на цвет полей")

if k % 2 == 0 and l % 2 == 0 or k % 2 == 1 and l % 2 == 1:
    color1 = 0
if k % 2 == 1 and l % 2 == 0 or k % 2 == 0 and l % 2 == 1:
    color1 = 1
if m % 2 == 0 and n % 2 == 0 or m % 2 == 1 and n % 2 == 1:
    color2 = 0
if m % 2 == 1 and n % 2 == 0 or m % 2 == 0 and n % 2 == 1:
    color2 = 1

logging.info("Началась проверка на совпадение цвета полей")

if color1 == color2:
    print("Фигуры находятся на полях одного цвета")
if color1 != color2:
    print("Фигуры находятся на полях разного цвета")

def ladya(k,l,m,n):
    logging.info("Началась функция ladya")

    global l_ugroza
    if k == m or l == n:
        l_ugroza = 1
    else:
        l_ugroza = 0

def l_output(l_ugroza):
    logging.info("Началась функция l_output")

    if l_ugroza == 1:
        print("Фигура 1 (ладья) угрожает фигуре 2")
    else:
        print("Фигура 1 (ладья) не угрожает фигуре 2")

def slon(k, l, m,n):
    logging.info("Началась функция slon")

    global s_ugroza
    if abs(k-m) == abs(l-n):
        s_ugroza = 1
    else:
        s_ugroza = 0

def s_output(s_ugroza):
    logging.info("Началась функция s_output")

    if s_ugroza == 1:
        print("Фигура 1 (слон) угрожает фигуре 2")
    else:
        print("Фигура 1 (слон) не угрожает фигуре 2")


def ferz(k,l,m,n):
    logging.info("Началась функция ferz")

    global f_ugroza

    if k == m or l == n:
        f1_ugroza = 1
    else:
        f1_ugroza=0

    if abs(k - m) == abs(l - n):
        f2_ugroza = 1
    else:
        f2_ugroza = 0

    if f1_ugroza == 1 or f2_ugroza == 1:
        f_ugroza = 1
    else:
        f_ugroza = 0

def f_output(f_ugroza):
    logging.info("Началась функция f_output")

    if f_ugroza == 1:
        print("Фигура 1 (ферзь) угрожает фигуре 2")
    else:
        print("Фигура 1 (ферзь) не угрожает фигуре 2")

def kon(k,l,m,n):
    logging.info("Началась функция kon")

    global k_ugroza
    if abs(k - m) * abs(l - n) == 2:
        k_ugroza = 1
    else:
        k_ugroza = 0

def k_output(k_ugroza):
    logging.info("Началась функция k_output")
    if k_ugroza == 1:
        print("Фигура 1 (конь) угрожает фигуре 2")
    else:
        print("Фигура 1 (конь) не угрожает фигуре 2")

print("Выберите фигуру 1")
logging.info("Началcя выбор фигуры")
while True:
    try:
        figura = int(input("Чтобы выбрать ладью нажмите 1, слона - 2, ферзя - 3, коня - 4: "))
        if figura > 4 or figura < 1:
            logging.error("Ошибка некорректного ввода")
            print("Такой фигуры нет")
        else:
            break
    except ValueError:
        logging.error("Ошибка некорректного ввода")
        print("Некорректный ввод")
        pass

if figura == 1:
    logging.info("Начался блок при выборе ладьи")
    ladya(k, l, m, n)
    l_output(l_ugroza)
    if l_ugroza == 1:
        print("С поля фигуры 1 (ладья) можно попасть на поле фигуры 2 за один ход")
    else:
        k_new=m
        l_new=n
        print("С поля фигуры 1 (ладья) нельзя попасть на поле фигуры 2 за один ход.\n"
              "Чтобы попасть на него можно сделать первый ход фигурой 1 на поле (", k_new, ":", l, ") или на поле (", k, ":",l_new,")" )


if figura == 2:
    logging.info("Начался блок при выборе слона")
    slon(k, l, m, n)
    s_output(s_ugroza)
    if s_ugroza == 1:
          print("С поля фигуры 1 (слон) можно попасть на поле фигуры 2 за один ход")
    elif s_ugroza == 0:
        if color1 == color2:
            if l < n:
                while True:
                    k = k - 1
                    l = l + 1
                    if abs(k - m) == abs(l - n):
                        k_new = k
                        l_new = l
                        print("С поля фигуры 1 (слон) нельзя попасть на поле фигуры 2 за один ход.\n"
                              "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                              ")")
                        break
            if l > n:
                while True:
                    k = k - 1
                    l = l - 1
                    if abs(k - m) == abs(l - n):
                        k_new = k
                        l_new = l
                        print("С поля фигуры 1 (слон) нельзя попасть на поле фигуры 2 за один ход.\n"
                          "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                          ")")
                        break
        else:
            print("Фигура 1 не сможет попасть на поле фигуры 2, т.к фигуры находятся на полях разного цвета")

if figura == 3:
    logging.info("Начался блок при выборе ферзя")
    ferz(k,l,m,n)
    f_output(f_ugroza)
    if f_ugroza == 1:
        print("С поля фигуры 1 (ферзь) можно попасть на поле фигуры 2 за один ход")
    else:
        if color1 == color2:
            if l < n:
                while True:
                    k = k - 1
                    l = l + 1
                    if abs(k - m) == abs(l - n):
                        k_new = k
                        l_new = l
                        print("С поля фигуры 1 (ферзь) нельзя попасть на поле фигуры 2 за один ход.\n"
                              "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                              ")")
                        break

            if l > n:
                while True:
                    k = k - 1
                    l = l - 1
                    if abs(k - m) == abs(l - n):
                        k_new = k
                        l_new = l
                        print("С поля фигуры 1 (ферзь) нельзя попасть на поле фигуры 2 за один ход.\n"
                              "Чтобы попасть на него можно сделать первый ход фигурой 1  на поле (", k_new, ":", l_new,
                              ")")
                        break
        else:
            k_new = m
            l_new = n
            print("С поля фигуры 1 (ферзь) нельзя попасть на поле фигуры 2 за один ход.\n"
                  "Чтобы попасть на него можно сделать первый ход фигурой 1 на поле (", k_new, ":", l,
                  ") или на поле (", k, ":", l_new, ")")

if figura == 4:
    logging.info("Начался блок при выборе коня")
    kon(k, l, m, n)
    k_output(k_ugroza)
    input("Нажмите Enter чтобы завершить программу.")
    logging.info("Программа завершилась")

