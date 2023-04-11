"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)###
100 -> 1 (1 + 0 + 0) |
"""
thr_dig_numb = str(input("Введите трехзначное число: "))
if str.isdigit(thr_dig_numb)==False or len(thr_dig_numb)!=3: print("Ты втираешь мне какую то дичь!!!")
else:
    summ = (int(thr_dig_numb[0])+int(thr_dig_numb[1])+int(thr_dig_numb[2]))
    print("Сумма цифр в вашем трехзначном числе = ",(summ))


