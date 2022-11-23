
from array import * #импорта модуля массива
a = array('i', [1, 2]) #объявление массива
print(a)
print(a.typecode) #TypeCode символ, использованный при создании массива

a.append(6)
print(a)

a.insert(1,7) #добавление в заданную позицию (по индексу)
print(a)

# расширение одного массива другим (должны быть одного типа, иначе ошибка).
# то же применимл к расширению массива списком
b = array('i', [4, 5, 6])
a.extend(b)
print(a)

dict_sample= {
1: 
    {'student1': 'Nicholas', 'student2': 'John', 'student3': 'Mercy'}, 
2:
    {'course1': 'Computer Science', 'course2': 'Mathematics', 'course3': 'Accounting'}
}

print(dict_sample[1]['student2'])