"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
"""
ticket=str(input("Введите номер билета: "))
if str.isdigit(ticket)==False: print("Увы, моншер! Задача подразумевает работу с числами!!!")
else:
    if (int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == (int(ticket[3]) + int(ticket[4]) + int(ticket[5])):
        print("Ваш билет - счастливый! Поздравляем!")
    else:
        print("У Вас хотя бы есть деньги на билет!")
