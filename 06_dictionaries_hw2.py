'''
    Проверьте, есть ли в словаре ключ country
    Выведите значение по-умолчанию 'Россия' для ключа country
    Добавьте в словарь элемент date со значением '27.05.2019'
    Выведите на экран длину словаря
'''

weather = {
    'city': 'Москва',
    'temperature': '20'
}

print('country' in weather)
print(weather.setdefault('country', 'Россия'))
weather['date'] = '27.05.2019'
print(weather)
print(len(weather))