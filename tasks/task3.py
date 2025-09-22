# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    weight = float(input("Введите число для значения weight: "))
    height = float(input("Введите число для height: "))
    bmi = weight / height ** 2
    print("Индекс: ", bmi)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()