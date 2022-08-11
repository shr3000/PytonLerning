"""
Банковский процент по вкладам составляет 1.5% в месяц. 
Процент начисляется каждый месяц на всю сумму-остаток на счету.
Пример вычисления процентов при вкладе в 10$:
1️⃣ месяц: 10$ + (10$ x 0.015) = 10,15$
2️⃣ месяц: 10.15$ + (10.15$ x 0.015) = 10,30$ 
3️⃣ месяц: 10.30$ + (10.30$ x 0.015) = 10,45$
Пользователь вводит с клавиатуры сумму вклада и на сколько месяцев он хочет положить деньги в банк. 

Программа должна вывести сумму, которая у него получиться по истечению этого срока на счету.
"""
cash = float(input("Enter you cash: "))
months = int(input("Enter number of months: "))
ithration = 1
while ithration <= months:
    cash = cash + (cash * 0.015)
    ithration = ithration + 1
print("Cash after", months,"in bank:", cash)