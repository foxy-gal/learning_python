months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь','июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
print(months)
empty_list = list('hello') #функция list, аргумент 'hello' разбивается на список - каждый символ - элемент списка)
print(empty_list)
print(len(empty_list)) #функция len выводит длину списка (кол-во элементов в списке)

#посчитать сумму чисел, входящих в список
done = [7, 10, 11, 9, 9, 6, 10]
a = done[0]+done[1]+done[2]+done[3]+done[4]+done[5]+done[6]
print(a)

#преобразовать список lst = ['11', 12, 'T', 'bee'] в [2, None, 1, 3]
lst = ['11', 12, 'T', 'bee']
lst = [len(lst[0]), None, len(lst[2]), len(lst[3])]
print(lst)

#Дан список lst, который содержит не менее элементов. Извлеките из него элементы ,  и  (начиная с ) в обратном порядке.
some_random_list = [1, 23, 00, 514, "cat"]
print(list[4:1:-1])

#Добавить в список новый элемент методом append
some_random_list.append(5)
some_random_list.append("breadgit")
print(some_random_list)
some_random_list.append("cat")

#удаление элемента из списка
some_random_list.remove(23)
print(some_random_list)
#list.remove("zombie") #попытка удалить то, чего нет в списке. Выдает ошибку "ValueError: list.remove(x): x not in list"
print(some_random_list)
some_random_list.remove("cat") #удаление элемента, который встречается больше раза в списке. удалил первый по порядку элемент
print(some_random_list)

#проверка на наличие элемента в списке
if 'груши'in some_random_list:
    some_random_list.remove('груши')
else:
    print('Груш в списке покупок нет')
    
#изменить существующий элемент списка - обратиться по индексу и ввести новое значение
some_random_list[1] = 23
print(some_random_list)

#конкатенация списков
list_of_purchase_wife = ['milk', 'bread', 'butter', 'condoms', 'wheat beer']
list_of_purchase_husband = ['gum', 'liquor', 'eggs']
general_purchase_list = list_of_purchase_wife + list_of_purchase_husband
print(general_purchase_list)

grocery = ['курица', 'яйца', 'молоко', 'бананы', 'вода','бананы','бананы']
guests_grocery = ['вино','сыр','сок']
new_grocery = grocery + guests_grocery 
print(new_grocery)

#сложение элементов списка - функция SUM(), int+float only
expanses = [100, 500.05, 250, 150]
print(sum(expanses))

#минимальное значение списка, максимальное - функции MIN() И MAX()
print(min(expanses))
print(max(expanses))
print(min(list_of_purchase_husband))
print(max(list_of_purchase_husband))

print(grocery.count('бананы'))

'''
Напишите код, принимающий на вход список transactions, 
в котором перечислены транзакции за покупки, 
совершенные пользователем. 
Задача программы — вывести на экран список из двух элементов. 
Первый элемент должен содержать количество покупок, а второй — максимальную стоимость покупки.
'''
transactions=[700, 800, 1100, 60, 80]
print(sum(transactions))
print(max(transactions))
interesting_metrics = [len(transactions), max(transactions)]
print(interesting_metrics)
#сортировка списка
temp = [20.5, 60, 77.9, 77, 0, 2, 45, 66.66]
print(sorted(temp))
print(sorted(temp, reverse = True))
temp.sort()
print(temp)
temp.sort(reverse=True)
print(temp)

#задача Напишите код, который преобразует список lst так, что вместо строковых элементов будет их длина, вместо остальных элементов — None.
lst = ['11', 12, 'T', 'bee']
empty_list = []

#простой цикл
for element in lst: #element - итератор, переменная в которую на каждую итерацию записывается элемент списка
    print(element)
    
print(element)

# цикл c if else
for element in lst: #element - итератор, переменная в которую на каждую итерацию записывается элемент списка
    if type(element) == str:
        empty_list.append(len(element))
    else: 
        empty_list.append(None)
print(empty_list)

#Необходимо определить самого опытного сотрудника в вашей команде. Напишите код, который выводит на экран список таких сотрудников.

experience = ['Вагнер', 7, 'Лисов', 3, 'Тихомиров', 12]
new_experience = max(experience[1::2])
for i, value in enumerate(experience): #enumerate - функция только в цикле для перебора по индексам и по значениям
    print(i)
    print(value)
    if value == new_experience:
        print(experience[i-1])