# MODULE 1

# В программу добавлен функционал:
# контроль ввода только одной цифры, а не числа (что соответствует заданию)

list_length = int(input('Введите количество элементов: '))
list_of_digits = []
for i in range(list_length):
    elem = input(f'Введите {i + 1}-й элемент: ')
    while not (elem.isdigit() and len(elem) == 1):
        elem = input('Элементом может быто только одна цифра! Попробуйте еще раз: ')
    list_of_digits.append(elem)
    elem = ''
list_of_digits.sort()
print (list_of_digits)