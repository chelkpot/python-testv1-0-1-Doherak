# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    a,b,c = map(int, input("Введите числа: "). split())
    num1 = a**2
    num2 = b**2
    num3 = c**2
    print("Результат:", num1, num2, num3)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()