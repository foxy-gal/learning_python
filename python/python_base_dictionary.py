employees = {'Мария А.': '+7(999)111-11-11', 'Иван И.': '+7(999)222-22-22','Сергей С.': '+7(999)333-33-33'}
print(employees)
print(type(employees))

#попытка создать словарь с одинаковым ключом
my_dict = {'a': 1,
       	            'a': 2}
print(my_dict)

#доступ к элементу словоря по ключу
print(employees["Мария А."])

#метод get(key, default_value)
print(employees.get('Мария А.', 55))
print(employees.get("Somebody", 77))

#добавление в словарь новых элементов
employees[11]=11
employees['mouse']='cheese'

#смена значения в словаре 
employees['Мария А.'] = 'хлебушек'
print(employees)

#удаление методом .POP()
print(employees.pop('Сергей С.')) #удаляет пару ключ-значение из словаря и возвращает удаленное значение +7(999)333-33-33
print(employees) #выводит массив уже без пары 'Сергей С.': '+7(999)333-33-33'

#удаление функцией DEL()
del(employees['Иван И.'])
print(employees)

#удаление(очищение всего словаря) методом .CLEAR()
employees.clear()
print(employees)

tenets_dict = {'Ильичев': 14, 'Антонов': 13}
print(tenets_dict.get('Ильичев',10))

#задача удалть Ильичев, добавить  Котов
tenants_dict = {'Иванов': 11, 'Петров': 12, 'Антонов': 13, 'Ильичев': 14}
tenants_dict.pop('Ильичев')
print(tenants_dict)
tenants_dict["Котов"] = 14
print(tenants_dict['Котов'])
#print(tenants_dict)
print(tenants_dict.keys())