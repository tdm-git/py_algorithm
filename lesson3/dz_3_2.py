"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6(или 0, 3, 4, 5 - если индексация начинается
 с нуля), т.к. именно в этих позициях первого массива стоят четные числа."""
sample_list = [8, 3, 15, 6, 4, 2]
result = []
for i, j in enumerate(sample_list):  # используем enumerate для получения значения и индекса
    if j % 2 == 0:
        result.append(i)
print(f'список индексов четных чисел для массива - {result}')
