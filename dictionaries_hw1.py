"""
    Создайте словарь:
    {"city": "Москва", "temperature": "20"}
    Выведите на экран значение ключа city
    Уменьшите значение "temperature" на 5
    Выведите на экран весь словарь
"""

weather = {
    "city": "Москва",
    "temperature": "20"
}

print(weather["city"])

weather["temperature"] = int(weather["temperature"]) - 5
print(weather["temperature"])

print(weather)
