# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел. Подсказка:
# факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count


def fibo_gen():
    for n in count(1):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        yield factorial


cycles = 15
for el in fibo_gen():
    print(el)
    cycles -=1
    if cycles == 0:
        break