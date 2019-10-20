# MODULE 3

# В программу добавлен дополнительный функционал:
# проверка на наличие недопустимых символов
# возможность вносить элементы в списки в несколько этапов
# на каждом этапе можно вводить числа как по одному, так и группами

sets = []
for num in range(2):
    sets.insert(num, set())
    print(f'Введите элементы {num + 1}-го списка:')
    no_more_elems = False
    while not no_more_elems:
        correct = 0
        while correct == 0:
            input_string = input('>>')
            if input_string.lower() != 'no':
                if input_string.isdigit():
                    temp_list = list(input_string)
                    correct = 1
                else:
                    splitter_mask = int(',' in input_string) + (int(';' in input_string) << 1) + (
                                int('/' in input_string) << 2)
                    splitter_sign = ''
                    if splitter_mask == 0:
                        if len(input_string) == 0:
                            print('Некорретный ввод! Введена пустая строка.')
                        else:
                            print('Некорретный ввод! Разделители не найдены.')
                    elif splitter_mask == 1:
                        splitter_sign = ','
                    elif splitter_mask == 2:
                        splitter_sign = ';'
                    elif splitter_mask == 4:
                        splitter_sign = '/'
                    else:
                        print('Некорретный ввод! Использовано несколько разделителей.')
                    if splitter_sign != '':
                        temp_list = input_string.split(splitter_sign)
                        correct = 1
                        for elem in temp_list:
                            if not elem.isdigit():
                                correct = 0
                        if correct == 0:
                            print('Некорретный ввод! В строке найдены недопустимые символы.')
                if correct == 1:
                    sets[num].update(set(temp_list))
                    temp_list = []
                print('Будут еще элементы? Введите их или наберите NO.')
            else:
                no_more_elems = True
                correct = 1
set_1_diff = sets[0] - sets[1]
list_diff = list(set_1_diff)
list_diff.sort()
print(f'Результат: {list_diff}.')