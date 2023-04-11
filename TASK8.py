"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
"""
choco_col=str(input("Введите ширину плитки шоколада: "))
choco_lin=str(input("Введите длинну плитки шоколада: "))
choco_pie=str(input("Введите количество квадратов для возможного отделения: "))
if int(choco_pie) > (int(choco_col)*int(choco_lin)): print("У Вас нет столько шоколада")
if str.isdigit(choco_col)==False or str.isdigit(choco_lin)==False or str.isdigit(choco_pie)==False: print("Увы, моншер! Задача подразумевает работу с числами!!!")
else:
    if (int(choco_pie) % int(choco_col)) == 0 or (int(choco_pie) % int(choco_lin)) == 0:
        print("Ломайте смело!")
    else:
        print("В любом случае фольгу не выбрасывайте!!!")