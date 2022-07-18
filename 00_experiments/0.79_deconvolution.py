import numpy as np
from typing import Union


def convert_from_str_to_ndarray_repr(str_mtrx: str) -> np.ndarray:
    """
    converts matrix represented by string where each row is space-separated
    :param str_mtrx: string
    :return: np.ndarray
    """
    return np.array([list(map(float, s)) for s in str_mtrx.split()])


def deconv(img: np.ndarray, fltr: np.ndarray) -> np.ndarray:
    img_dim, fltr_dim = img.shape[0], fltr.shape[0]
    new_dim = img.shape[0] + fltr.shape[0] - 1

    deconv_img = np.zeros((new_dim, new_dim), dtype=float)

    for i in range(img_dim):
        for j in range(img_dim):
            deconv_img[i:i+fltr_dim, j:j+fltr_dim] += fltr * img[i, j]

    return deconv_img


if __name__ == '__main__':
    img = '01110 10001 01110 10101 01110'
    fltr = '010 111 010'

    img = convert_from_str_to_ndarray_repr(img)
    fltr = convert_from_str_to_ndarray_repr(fltr)
    deconv_img = deconv(img, fltr)

    look_for = 3.0
    count = (np.isclose(deconv_img, look_for)).sum()

    print(deconv_img)
    print(f'{count} pixels in conv_img are equal to {look_for}')
