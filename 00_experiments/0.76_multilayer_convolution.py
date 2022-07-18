import numpy as np
from typing import Union


def apply_filter(img: Union[str, np.ndarray], fltr: Union[str, np.ndarray], padding=0, stride_x=1, stride_y=1) -> np.ndarray:
    if isinstance(img, str):
        img = np.array([list(map(float, s)) for s in img.split()])

    if padding:
        img = np.pad(img, pad_width=padding)

    if isinstance(fltr, str):
        fltr = np.array([list(map(float, s)) for s in fltr.split()])

    # print(f'initial image matrix:\n{img}')
    # print(f'mask:\n{mask}')

    # Если у нас имеется фильтр размера AxB, изображение CxD и страйды XxY,
    # то результирующее изображение после свёртки будет размера ((C-A+Y)//Y)x((D-B+X)//X).
    # Для страйдов по умолчанию размер будет иметь размерность (C-A+1)x(D-B+1).
    # Заготовка для матрицы после свёртки с соответствующей размерностью.
    res_matrix_size = ((img.shape[0] - fltr.shape[0] + stride_y) // stride_y,
                       (img.shape[1] - fltr.shape[1] + stride_x) // stride_x)
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
            mtx = img[i * stride_y:i * stride_y + fltr.shape[0], j * stride_x:j * stride_x + fltr.shape[1]]

            # element-wise multiplication of current slice 'mtx' and 'mask'
            # and subsequent summation of all elements of resulting matrix
            result_mtrx[i, j] = (mtx * fltr).sum()

    # Вид результирующей матрицы
    # print('Вид результирующей матрицы:')
    # print(result_mtrx)
    # print()

    # Число строк и столбцов в результирующем изображении
    # print(f'Matrix size: {result_mtrx.shape[0]}X{result_mtrx.shape[1]}')
    # print()

    return result_mtrx


if __name__ == '__main__':
    # Матрица исходного изображения как строка, состоящая из последовательностей символов, разделенных пробелом
    img_str = '01010 00100 11011 11111 01110'

    # список применяемых фильтров, заданный в таком же формате, как и исходное изображение 'img_str'
    # используем 3 одноканальных фильтра, каждый из них применяем независимо к исходному ихображению
    filters_lst = [
        '100 010 001',
        '111 111 111',
        '001 010 100'
    ]

    # к исходному изображению применяем каждый из 3-х одноканальных фильтров НЕЗАВИСИМО от других
    # на выходе получаем 3-канальное изображение (3 новых канала изображения)
    # исходное изображение расщепилось на 3 канала
    img_3_channels = [apply_filter(img_str, fltr) for fltr in filters_lst]
    for i, f_channel in enumerate(img_3_channels, start=1):
        print(f'Channel {i}:\n{f_channel}')
        print()
    """
    Каждый фильтр отработал независимо от других и исходная картинка расщепилась на 3 канала
        Channel 1:     Channel 2:     Channel 3:
        [[0. 3. 1.]    [[4. 5. 4.]    [[1. 3. 0.]
        [2. 1. 3.]     [6. 6. 6.]     [3. 1. 2.]
        [3. 3. 1.]]    [7. 8. 7.]]    [1. 3. 3.]]
    """

    # Поскольку картинка теперь 3-канальная, то мы обязаны применять к ней 3-канальный фильтр
    # задаем 3-х канальный фильтр; каждый канал фильтра: np.ndarray размера 1x1
    filter_channels = [np.array([1])[:, np.newaxis], np.array([-1])[:, np.newaxis], np.array([1])[:, np.newaxis]]

    # каждый канал фильтра применяется к соответствующему каналу изображения
    # в результате получаем 3 свертки по каждому каналу: 'conv'
    conv = np.array([apply_filter(img_3_channels[i], f_channel) for i, f_channel in enumerate(filter_channels)])

    # на последнем шаге свертки по каждому каналу суммируются поэлементно
    # итоговая свертка многоканального изображения получается ОДНОКАНАЛЬНОЙ
    res_convolution = np.sum(conv, axis=0)
    print(f'res_convolution:\n{res_convolution}')



