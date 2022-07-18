import numpy as np
from typing import Union


def apply_filter(img: Union[str, np.ndarray], fltr: str, padding=0, stride_x=1, stride_y=1) -> np.ndarray:
    if isinstance(img, str):
        img = np.array([list(map(float, s)) for s in img.split()])

    if padding:
        img = np.pad(img, pad_width=padding)

    mask = np.array([list(map(float, lst)) for lst in fltr.split()])
    print(f'initial image matrix:\n{img}')
    print(f'mask:\n{mask}')

    # Если у нас имеется фильтр размера AxB, изображение CxD и страйды XxY,
    # то результирующее изображение после свёртки будет размера ((C-A+Y)//Y)x((D-B+X)//X).
    # Для страйдов по умолчанию размер будет иметь размерность (C-A+1)x(D-B+1).
    # Заготовка для матрицы после свёртки с соответствующей размерностью.
    res_matrix_size = ((img.shape[0] - mask.shape[0] + stride_y) // stride_y,
                       (img.shape[1] - mask.shape[1] + stride_x) // stride_x)
    result_mtrx = np.zeros(res_matrix_size)

    # Операция свёртки
    # Проход по строкам результирующей матрицы
    for i in range(result_mtrx.shape[0]):
        # Проход по столбцам матрицы.
        for j in range(result_mtrx.shape[1]):
            """ 
            Поэлементная свёртка изображения:
            Из матрицы img берётся срез по строкам и столбцам, такой же размерности как и у фильтра mask.
            Элементы из подматрицы перемножаются с элементами фильтра (не матричное умножение).
            После чего, все элементы полученной матрицы суммируются и результат записывается
            в матрицу result_mtrx i-ую строку и j-ый столбец, с учётом смещения по страйдам.
            """
            # get current slice in 'result_mtrx'
            mtx = img[i * stride_y:i * stride_y + mask.shape[0], j * stride_x:j * stride_x + mask.shape[1]]

            # element-wise multiplication of current slice 'mtx' and 'mask'
            # and subsequent summation of all elements of resulting matrix
            result_mtrx[i, j] = (mtx * mask).sum()

    # Вид результирующей матрицы
    print('Вид результирующей матрицы:')
    print(result_mtrx)
    print()

    # Число строк и столбцов в результирующем изображении
    print(f'Matrix size: {result_mtrx.shape[0]}X{result_mtrx.shape[1]}')
    print()

    return result_mtrx


if __name__ == '__main__':
    # Матрица исходного изображения задается как строка, состоящая из последовательностей char, разделенных пробелом
    # img_str = '0111 0111 1110 0101'
    # fltr_str_1 = '01 10'
    # fltr_str_2 = '11'

    img_str = '110 011 110'

    # fltr_str_1 = '11'
    # fltr_str_2 = '0 1'
    fltr_str_1 = '1 1'
    fltr_str_2 = '01'

    result_mtrx1 = apply_filter(img_str, fltr_str_1)
    result_mtrx2 = apply_filter(result_mtrx1, fltr_str_2)

    # Значение, которое необходимо найти в конечной матрице.
    value2search = 5
    # Поиск и подсчёт количества совпадений.
    print(f'Элементов, равных {value2search} найдено {len(result_mtrx2[result_mtrx2 == value2search])}')
    print()

    # Сумма всех значений результирующей матрицы
    print(f'Сумма всех значений матрицы: {result_mtrx2.sum()}')

    value = 5.0
    print(f'The number of elements with value = {value}: {np.isclose(result_mtrx2, 5.0).sum()}')







