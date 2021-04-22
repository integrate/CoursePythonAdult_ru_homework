"""
В супермаркете проходит акция: 3 шоколадки по цене 2х.
Т.е. при покупке 2х шоколадок третью дают в подарок.

Каждая шоколадка стоит X1 рублей.
У покупателя есть X2 рублей.

Сколько шоколадок он получит на эти деньги.
Сколько непотраченных денег останется у покупателя.
Программа должна вывести решение с объяснением.
"""

all_money = 100
one_item_price = 17

pairs_of_items =all_money//(one_item_price*2)
money_after_pairs = all_money%(one_item_price*2)
items_without_gifts = money_after_pairs//one_item_price
money_final = money_after_pairs%one_item_price

print("Всего у покупателя", all_money)
print("Одна шоколадка стоит", one_item_price)

print("На эти деньги он купит", pairs_of_items, "пар шоколадок, т.е.",pairs_of_items*2, "штук")
print("Ему в подарок дадут еще", pairs_of_items, "шоколадок, т.е. всего",pairs_of_items*3, "штук")
print("У него останется", money_after_pairs,"денег")
print("Этого хватит еще на", items_without_gifts,"шоколадок")
print("Итого он купит", pairs_of_items*3+items_without_gifts,"шоколадок")
print("После этого у него останется", money_final,"денег")