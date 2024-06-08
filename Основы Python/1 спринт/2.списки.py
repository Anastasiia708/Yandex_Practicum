"""""
russian_alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

print(russian_alphabet[1])  # Напечатать значение элемента с индексом 1
print(russian_alphabet[2])  # Напечатать значение элемента с индексом 2

# значение последнего элемента
count = len(russian_alphabet)
print(count)
print(russian_alphabet[count - 1]) # Будет напечатано: я

#обратиться к предпоследним элементам
print(russian_alphabet[count - 2]) # Будет напечатано: ю

print(russian_alphabet[-2]) # Будет напечатано: ю
print(russian_alphabet[-4]) # Будет напечатано: ь

print(russian_alphabet[26]) # Будет напечатано: ь



priority = [1,2,3]
# укажи индекс среднего приоритета
print('Баг с приоритетом:', priority[1])


#Добавить элемент: метод append()
# создали список из одного элемента — хоббита Фродо
hobbits = ['Фродо']
# добавили ещё одного хоббита
hobbits.append('Сэм')
# вдвоём кольцо станет нести легче
print(hobbits) # Будет напечатано: ['Фродо', 'Сэм']


#Добавить элемент на указанную позицию: метод insert()
hobbits = ['Фродо', 'Сэм', 'Мерри', 'Пиппин']
hobbits.insert(2, 'Смеагол')
print(hobbits) #['Фродо', 'Сэм', 'Смеагол', 'Мерри', 'Пиппин']

#Удалить элемент по значению: метод remove()
hobbits.remove('Смеагол')
print(hobbits) #['Фродо', 'Сэм', 'Мерри', 'Пиппин']


#Удалить элемент по индексу: метод pop()
hobbits = ['Фродо', 'Cэм', 'Мерри', 'Пиппин']
one_hobbit = hobbits.pop(-2)  # В одно действие удалили Мерри из hobbits и сохранили его в новой переменной
print(hobbits)  # ['Фродо', 'Cэм', 'Пиппин']
print(one_hobbit) # Мерри


#Если не передать в pop() индекс, метод по умолчанию удалит и вернёт последний элемент.
hobbits = ['Пиппин', 'Фродо', 'Сэм']
hobbits.pop()   # 'Cэм'
print(hobbits)  # ['Пиппин', 'Фродо']


#Значение, которое удаляет pop(), можно сразу добавить в другой список.
lst_1 = ['pen']
lst_2 = ['apple']
# Подхватили 'pen', удалили из lst_1, вернули в код и тут же добавили в список lst_2
lst_2.append(lst_1.pop())
print(lst_1) # Будет напечатано: []
print(lst_2) # Будет напечатано: ['apple', 'pen']




hobbits = ['Cэм', 'Пиппин']
lst = ['Мерри', 'Фродо']
# удали из lst Фродо и верни его в начало списка hobbits
hobbits.insert(0,lst.pop(-1))
print(hobbits) #['Фродо', 'Cэм', 'Пиппин']
print(lst) #['Мерри']

print('Смеагол' in hobbits)   # False





#сложение списков
# стартовый набор
hobbits = ['Фродо', 'Сэм', 'Мерри', 'Пиппин']
# новый набор
new_members = ['Гэндальф', 'Арагорн']
# объединение списков
fellowship = hobbits + new_members
print(fellowship) #['Фродо', 'Сэм', 'Мерри', 'Пиппин', 'Гэндальф', 'Арагорн']


hobbits = ['Фродо', 'Cэм']
eagles = ['Орёл 1', 'Орёл 2']
# добавить орлов в список
hobbits.insert(2, eagles)
print(hobbits)
# ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]



#Поверхностное копирование: метод copy()
hobbits = ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]
# скопировали его
new_hobbits_list = hobbits.copy()
# логическим оператором проверили равенство списков:
print(new_hobbits_list == hobbits)
# Будет напечатано True
print(new_hobbits_list)
# Будет напечатано: ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]


new_hobbits_list[2].append('Орёл 3') # Добавили орла для Бильбо
print(new_hobbits_list)
# Будет напечатано: ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2', 'Орёл 3'], 'Бильбо']
# в этот раз оригинальный список поменяется
print(hobbits)
# Будет напечатано: ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2', 'Орёл 3']]




#Полное копирование: метод deepcopy()
#Чтобы использовать, его нужно импортировать.
# Для этого добавляют команду from copy import deepcopy.
from copy import deepcopy # импортировали метод deepcopy из модуля copy
# создали заново список
hobbits = ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]
# сделали полную копию
new_hobbits_list = deepcopy(hobbits)
print(hobbits, new_hobbits_list)
# Будет выведено: ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']], ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]
# теперь изменили копию
new_hobbits_list.append('Бильбо')
new_hobbits_list[2].append('Орёл 3')
print(new_hobbits_list)
# Будет выведено: ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2', 'Орёл 3'], 'Бильбо']
print(hobbits)
# Будет выведено: ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]
"""""



priority = ['Значительный', 'Средний', 'Тривиальный']

severity = ['Низкий', 'Незначительный', 'Блокирующий', 'Высокий', 'Критический']

priority.insert(0,severity.pop(-2))
priority.insert(-1,severity.pop(0))
severity.append(priority.pop())
severity.insert(2, priority.pop(1))
severity.insert(-2, severity.pop(0))
severity.insert(1,severity.pop(-2))
print(priority)
# Должно получиться:
# ['Высокий', 'Средний', 'Низкий']
print(severity)
# Должно получиться:
# ['Блокирующий', 'Критический', 'Значительный', 'Незначительный', 'Тривиальный']

