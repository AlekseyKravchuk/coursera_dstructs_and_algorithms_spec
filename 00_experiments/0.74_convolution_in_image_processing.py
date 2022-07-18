import numpy as np


if __name__ == '__main__':
    # Матрица исходного изображения задается как строка, состоящая из последовательностей char, разделенных пробелом
    # img_str = '00000000 01110000 01111000 01111100 00111110 00011111'
    img_str = '0101010 1111111 0101010 1111111 0101010'
    padding = 1

    # Преобразуем исходную матрица в numpy-array типа float
    img = np.array([list(map(float, s)) for s in img_str.split()])
    if padding:
        img = np.pad(img, pad_width=1)

    fltr = '010 111 010'
    mask = np.array([list(map(float, lst)) for lst in fltr.split()])

    print(f'mask:\n{mask}')

    # Страйды по x и y, если не заданы, то оставляйте по умолчанию
    stride_x = 2  # По умолчанию равно 1
    stride_y = 2  # По умолчанию равно 1

    # Если у нас имеется фильтр размера AxB, изображение CxD и страйды XxY,
    # то результирующее изображение после свёртки будет размера ((C-A+Y)//Y)x((D-B+X)//X).
    # Для страйдов по умолчанию размер будет иметь размерность (C-A+1)x(D-B+1).
    # Заготовка для матрицы после свёртки с соответствующей размерностью.

    res_matrix_size = ((img.shape[0] - mask.shape[0] + stride_y) // stride_y,
                       (img.shape[1] - mask.shape[1] + stride_x) // stride_x)
    result = np.zeros(res_matrix_size)
    # print(f'result:\n{result}')
    # print(res_matrix_size)

    # Операция свёртки
    # Проход по строкам результирующей матрицы
    for i in range(result.shape[0]):
        # Проход по столбцам матрицы.
        for j in range(result.shape[1]):
            # Поэлементная свёртка изображения:
            # Из матрицы img берётся срез по строкам и столбцам, такой же размерности как и у фильтра mask.
            # Элементы из подматрицы перемножаются с элементами фильтра (не матричное умножение).
            # После чего, все элементы полученной матрицы суммируются и результат записывается
            # в матрицу result i-ую строку и j-ый столбец, с учётом смещения по страйдам
            mtx = img[i * stride_y:i * stride_y + mask.shape[0], j * stride_x:j * stride_x + mask.shape[1]]
            result[i, j] = (mtx * mask).sum()

    # Вид результирующей матрицы
    print('Вид результирующей матрицы:')
    print(result)
    print()

    # Число строк и столбцов в результирующем изображении
    print(f'Matrix size: {result.shape[0]}X{result.shape[1]}')
    print()

    # Значение, которое необходимо найти в конечной матрице.
    find = 5
    # Поиск и подсчёт количества совпадений.
    print(f'Элементов, равных {find} найдено {len(result[result == find])}')
    print()

    # Сумма всех значений результирующей матрицы
    print(f'Сумма всех значений матрицы: {result.sum()}')

    value = 5.0
    print(f'The number of elements with value = {value}: {np.isclose(result, 5.0).sum()}')







