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
list = [1, 23, 00, 514, "cat"]
print(list[4:1:-1])

#Добавить в список новый элемент методом append
list.append(5)
list.append("breadgit")
print(list)

#удаление элемента из списка
list.remove(23)
print(list)