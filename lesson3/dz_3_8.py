"""Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""
result = []  # результатом будет двухмерный массив
sum_ch = 0
line_list = []
for i in range(1, 17):
    user_choise = int(input('введите значение элемента матрицы  - '))
    line_list.append(f'{user_choise:>5}')  # добавим небольшое форматирование
    sum_ch += user_choise
    if i % 4 == 0:  # после 4го элемента добавляем сумму и обнуляем промежуточный список
        line_list.append(sum_ch)
        result.append(line_list)
        sum_ch = 0
        line_list = []
for i in result:  # выводим результат
    print(*i)     # используем оператор "распаковки" для вывода строки матрицы
