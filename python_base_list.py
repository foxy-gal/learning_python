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