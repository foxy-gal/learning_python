#Необходимо определить самого опытного сотрудника в вашей команде. Напишите код, который выводит на экран список таких сотрудников.

experience = ['Вагнер', 7, 'Лисов', 3, 'Тихомиров', 12]
new_experience = max(experience[1::2])
for i, value in enumerate(experience): #enumerate - функция только в цикле для перебора по индексам и по значениям
    #print(i) #перебирает индексы
    #print(value) #перебирает значения
    if value == new_experience: #если значение =максимальному в срезе
        print(experience[i-1]) 

#Вывести элементы списка по шаблону "Элемент 5"
my_list = [5, 9, 'hui']
for element in my_list:
    print(f'Element {element}')

#Оказалось можно по-простому, без f'
my_list = [5, 9, 'hui']
for element in my_list:
    print('Element', element)
    
#Дан список доходов членов семьи Быковых incomes (в тысячах рублей)
#Необходимо найти общий доход семьи.
incomes = [120, 38.5, 40.5, 80]

#Итерируемый объект incomes
#Тело цикла - сложить текущее итерируемое + текущее итерируемое

s = 0
for i in incomes:
    s += i
print(s)