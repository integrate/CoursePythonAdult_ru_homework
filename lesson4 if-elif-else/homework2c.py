"""
Уровень Головоломка:
Решить задачу с любым количеством вишен, используя один if, один elif и один else.
Т.е. решение должно выглядеть как

answer = int(input("Сколько вишен вы хотите съесть?"))

if <условие>:
  print(...)
elif <условие>:
  print(...)
else:
  print(...)
"""

answer = input("Сколько вишен вы хотите съесть?")
answer = int(answer)

if answer % 10 == 1 and answer // 10 != 1:
    print("Вы съели " + str(answer) + " вишню")

elif 1 < answer % 10 <= 4 and answer // 10 != 1:
    print("Вы съели " + str(answer) + " вишни")

else:
    print("Вы съели " + str(answer) + " вишен")
