genjutsu = {"Tsukyemi":7, "illusion":1}
# vowels keys

sharingan = {'g': None, 'e': None, 'n': None, 'j': None, 'u': None, 't': None, 's': None, 'u': None}
value = [1]

uchiha = {'имя': "Итачи", "age": 21}

sf = {'ruin': 2, 'feed': 3, 'loose': 4}
items = sf.items()


if __name__ == '__main__':
    # dict.clear
    a = {1: "Madara", 2:"Hashirama"}
    a.clear()  # очищает словарь.
    print(a)

    # dict.copy возвращает копию словаря.
    copied_genjutsu = genjutsu.copy()
    print('Genjutsu', genjutsu)
    print('copied genjutsu', genjutsu)

    # dict.fromkeys создает словарь с ключами из seq и значением value (по умолчанию None).
    madara = {sharingan: list(value) for sharingan in sharingan}
    print(madara)

    # dict.get возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
    print('Имя: ', uchiha.get('имя'))
    print("Age: ", uchiha.get("age"))
    print('Томое в шарингане ', uchiha.get('Томое в шарингане', 'есть'))
    print('Томое в шарингане ', uchiha.get('Томое в шарингане ', 3))

    #dict .items  возвращает пары (ключ, значение).
    print("original items", items)
    del[sf['ruin']]
    print('Update items', items)

    # dict.keys возвращает ключи в словаре.
person = {'name': 'Phill', 'age': 22, }

print('До обновления словаря')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nПосле обновления словаря')
print(keys)

# dict.pop удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
hero = {'salo': 2, 'pudge': 3, 'monkey king': 4 }
element = hero.pop('salo')
print('Удаленный элемент', element)
print('Словарь', hero)

# dict.popitem удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
person = {'name': 'Itachi', 'age': 21, 'tomoe sharingan': 3}
# ('зарплата', 3500.0) вставляется последней, поэтому она удаляется
result = person.popitem()

print('Возвращаемое значение = ',result)
print('человек=', person)
# # вставляем новую пару элементов
person['профессия'] = 'Водопроводчик'
# now ('профессия', 'сантехник') - последний элемент
result = person.popitem()
print('Возвращаемое значение')
print('человек', person)

# dict.setdefault возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
uchiha = {'name': 'Itachi'}
# ключа нет в словаре
salary = uchiha.setdefault('salary')
print('uchiha = ',uchiha)
print('salary = ',salary)

# ключа нет в словаре
# Предоставляется # default_value значение по умолчанию
age = uchiha.setdefault('age', 21)
print('uchiha = ',uchiha)
print('age =', age)


# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
d = {1: "one", 2: "three"}
d1 = {2: "two"}
#обновляет значение ключа 2
d.update(d1)
print(d)
d1 ={3: "three"}
# добавляет элемент с ключом 3
d.update(d1)

print(d)

# dict.values() - возвращает значения в словаре
dota = {'tilt': 2, 'nervy': 3, 'gorenie': 4 }
value = dota.values()
print('Оригинальные предметы:', value)
# удалить элемент из словаря
del[dota['tilt']]
print('Обновленные предметы:', value)

# отдельное домашнее задание
b = {}
b[float('nan')] = 1
b[float('nan')] = 2
b[1.0] = 'float'
b[1] = 'int'
b[True] = 'bool'
print(b)  # Длина словаря будет 3