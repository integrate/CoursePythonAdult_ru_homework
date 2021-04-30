"""
Более сложный вариант:
Доделать программу, чтобы она работала с любым количеством вишен от 0 до бесконечности.
"""

answer = input("Сколько вишен вы хотите съесть?")
answer = int(answer)

if answer == 0:
    print("Вы съели 0 вишен")

elif answer == 1:
    print("Вы съели одну вишню")

elif answer <= 4:
    print("Вы съели " + str(answer) + " вишни")

elif answer <= 20:
    print("Вы съели " + str(answer) + " вишен")

elif answer % 10 == 0:
    print("Вы съели " + str(answer) + " вишен")

elif answer % 10 == 1:
    print("Вы съели " + str(answer) + " вишню")

elif answer % 10 <= 4:
    print("Вы съели " + str(answer) + " вишни")

else:
    print("Вы съели " + str(answer) + " вишен")