"""""
best_movies = ['Побег из Шоушенка', 'Криминальное чтиво', 'Форрест Гамп', 'Леон', 'Король Лев']

for movie in best_movies: # Это условие цикла
    print(movie) # А это тело цикла


friends = ['Артём', 'Катя', 'Егор', 'Настя', 'Петя', 'Илья', 'Саша']
for friend in friends:
    print('Имя ' + friend + ' состоит из ' + str(len(friend)) + ' букв.') #Имя Артём состоит из 5 букв.


five = range(0,6) # Последовательность включает 0, 1, 2, 3, 4 и 5
also_five = range(6) # Такая же последовательность
print(five == also_five) # Проверили логическим оператором
# Будет напечатано: True


step_size_2 = range(1, 7, 2)
# Указали начало последовательности (1), её конец (7) и шаг = 2
# step_size_2 будет включать числа 1, 3, 5 



around_zero = range(-3, 3)
for i in around_zero:
    # Перебрать все числа в диапазоне от -3 до 3 и напечатать их:
    print(i)
# Будет напечатано:
# -3
# -2
# -1
# 0
# 1
# 2 
    
   

rooms_floor1 = ['Номер 1', 'Номер 2', 'Номер 3', 'Номер 4']
rooms_floor2 = ['Номер 5', 'Номер 6', 'Номер 7', 'Номер 8']
rooms_floor3 = ['Номер 9', 'Номер 10', 'Номер 11', 'Номер 12']

hotel_floors = [rooms_floor1, rooms_floor2, rooms_floor3]

for floor_rooms in hotel_floors: # Запустили внешний цикл по списку hotel_floors
    # тело внешнего цикла
    for room in floor_rooms: # Создали вложенный цикл для хождения по списку номеров, который записан в переменную
        # тело вложенного цикла
        print('Убрать', room) # Вывели номер номера на каждом шаге вложенного цикла
    # тело внешнего цикла
    print('Подняться на этаж выше') # Вывели сообщение о переходе на следующий этаж на каждом шаге внешнего цикла




shelf1 = ['клубничное варенье', 'вишнёвое варенье']
shelf2 = ['грушевое варенье', 'абрикосовое варенье']

closet = [shelf1, shelf2]

print('Привет, Карлсон!')
print('Смотри, у меня с собой:')

for shelf in closet:
    for jam in shelf:
        print(jam)



streets_city1 = ['улица Строителей', 'улица Правды', 'улица Свободы']
streets_city2 = ['улица Строителей', 'улица Программистов', 'улица Счастья']
streets_city3 = ['улица Строителей', 'улица Веселья', 'улица Добра']

cities = [streets_city1, streets_city2, streets_city3]

for city in cities:
    for street in city:
        print(street)



#цикл с условием
nums = 0
for i in range(0, 11,2): #0,2,6,8
    if i < 8 and i != 4:
        nums += i
print(nums) #0 + 2 + 6 = 8, цикл плюсанул к nums числа меньше 8 и не равные 4 с шагом 2, т.е. 2 и 6



clients = [19, 22, 42, 28, 69, 51, 18, 70]
clients_found = 0
for i in clients:
    if i > 21 and i < 60:
        clients_found += 1
print(clients_found)


numbers = [0,2,6,8,10]
nums = 0
for i in numbers:
    if i < 8 and i != 4:
        nums += i
print(nums)
"""""
