# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (¬ отрицание, ⋀ и, ⋁ или)


x = float(input('Введите число x '))
y = float(input('Введите число y '))
z = float(input('Введите число z '))
a = x * y * z
print(a)
b = x + y + z
print(b)
if a > 0:
    a = 0
elif a < 1:
    a = 1
if b > 0 or b < 1:
    b = 1
if a == b:
    print('истина')
elif a != b:
    print('ложь')