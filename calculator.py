inpWord = input()
if inpWord == 'Сложение': print(int(input()) + int(input()))
elif inpWord == 'Вычитание':print(int(input()) - int(input()))
elif inpWord == 'Умножение':print(int(input()) * int(input()))
elif inpWord == 'Деление нацело':print(int(input()) // int(input()))
elif inpWord == 'Вычисление остатка':print(int(input()) % int(input()))
elif inpWord == 'Возведение в степень':
    x = int(input())
    u = x
    for i in range(int(input())):
        x *= u
    print(x)
elif inpWord == 'Корень второй степени':
    x = int(input())
    y = x * x
    print(y * y)