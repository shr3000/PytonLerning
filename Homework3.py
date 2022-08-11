"""
Кофе стоит 5, круасан 3. Пользователь вводит с клавиатуры сколько у него денег
нужно посчитать хватит ему на кофе с круасаном или нет.
Если денег мало, то хватит ли на кофе без круасана?
Круасан отдельно не нужен 
"""
amount = int (input("how much money do you have?: "))
if amount > 8 :
    print ("Get your coffee with croissant")
elif amount < 8 and amount >=5 :
    print ("Your money is only enough for coffee")
elif amount < 5:
    print("Go past yourself. Today is not a charity day.")
