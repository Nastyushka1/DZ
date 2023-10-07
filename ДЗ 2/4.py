x = input()
y = x.count('(')
n = x.count (')')
if y > n:
    print(f"Не хватает {y - n} закрывающих скобок!")
elif n > y:
    print(f"Не хватает {n - y} открывающих скобок!")
else:
    print("Все правильно!")