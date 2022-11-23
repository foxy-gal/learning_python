#
python = ['Аня', 'Вася', 'Петя']
ml = ['Аня']
maths = ['Катя', 'Женя', 'Вася']
all_students = python + ml + maths
print(all_students)

#обращение в множество 0 запись в новую переменную
unique_students = set(all_students)
print(unique_students)

#Пустое множество можно создать только с помощью функции set() без аргументов
empty = {}
print(type(empty))
empty_set = set()
print(type(empty_set))

#проверка есть ли в множестве проверяемое значение
print('Катя' in all_students)
print(11 in all_students)

#добавление новых элементов в set Метод .ADD()
print(unique_students)
unique_students.add("Mango")
print(unique_students)

#добавление новых элементов в set Метод .UPDATE()
random_set = {11, "kiwi", 'kiss', True, 0.6}
unique_students.update(random_set)
print(unique_students)

#удаление элементов из set Метод .REMOVE()
unique_students.remove('kiwi')
print(unique_students)

#удаление элементов из set Метод .DISCARD()
unique_students.remove(0.6)
print(unique_students)

#сравнение методов
unique_students.discard('Иннокентий')
print(unique_students)
#unique_students.remove('Иннокентий')
print(unique_students)

#объединение множеств
python = {'Лена', 'Андрей', 'Катя'}
print(python.union(ml))

#пересечение множеств
ml = {'Саша', 'Лена'}

#нахождение пересечения метод .INTERSECTION
print(ml.intersection(python))

#короткий вариант получения пересечения множеств
print(python&ml) 

#разность множеств метод .DIFFERENCE  
print(python.difference(ml))

#симметричное множество метод .SYMMETRIC_DIFFERENCE
print(ml.symmetric_difference(python))

#короткий способ получить симметричное множество ^
print(python^ml)

#задача вывести список уникальных элементов 
fruits = ['яблоко', 'груша', 'яблоко', 'апельсин']
set_fruits = set(fruits)
print(len(set_fruits))

# Напишите программу, принимающую на вход список фруктов fruits. 
# Напишите функцию, которая выведет на экран список уникальных элементов в алфавитном порядке.
fruits = ['яблоко', 'груша', 'апельсин', 'груша', 'дыня', 'груша']
set_fruits = set(fruits)
print(sorted(list(set_fruits)))


# Определите, сколько в нем встречается различных чисел.
numbers = [1,2,4,3,6,8,4,5,9,1]
print(len(set(numbers)))

string1_set=set('string1')
print(string1_set)

string2_set=set('string2')
print(string2_set)
print(string1_set.intersection(string2_set))