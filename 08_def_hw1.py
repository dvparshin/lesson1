"""
    Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает объединенными через разделитель delimiter
    Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
    Сделайте так, чтобы результирующая строка выводилась заглавными буквами
"""

def get_summ(one, two, delimiter='&'):
    # return str(one) + delimiter + str(two)
    concatinate_string = f'{one} {delimiter} {two}'
    return concatinate_string

print(get_summ('Learn', 'python').upper())
