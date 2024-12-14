def print_params(a = 1, b = 'Здравствуйте Орехов С.С.', c = True):
    print(a, b, c)

print_params()

#Вызов функции print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(4, 'Всего доброго Орехов С.С.', False)
print_params(7, 'Сирица')
print_params(a='1', b='9', c='33')
print_params(a= 2, b= 4)
print_params(a='Единичка', c= 7)
print_params(a='Какой-то набор букв')
print_params()

#Проверка, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25)
print_params(c=[1, 2, 3])

#Создание списка values_list с тремя элементами разных типов.
values_list = [1, "Список", 7.5]
values_dict = {'a':1, 'b':'Институт Urban', 'c':True}
print_params(*values_list)
print_params(**values_dict)

#Создание списка values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка']
#Проверка, работает ли print_params(*values_list_2, 42)
print(*values_list_2, 42)