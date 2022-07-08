"""
Author: Matthias Mühleder
Matr.Nr.: K12110857
Exercise 4
"""
import numpy as np
import torch




def check_int_obj(tuple, lowerbound, upperbound):
    try:
        for value in tuple:
            if not lowerbound <= int(value) <= upperbound:
                raise ValueError
    except ValueError:
        raise ValueError
    return


def ex4(image_array, offset, spacing):
    if not isinstance(image_array, np.ndarray):
        raise TypeError
    if not len(image_array.shape) == 3:
        raise NotImplementedError
    if not image_array.shape[2] == 3:
        raise NotImplementedError

    check_int_obj(tuple=offset, lowerbound=0, upperbound=32)
    check_int_obj(tuple=spacing, lowerbound=2, upperbound=8)

    image_array_trans = np.transpose(image_array, (2, 0, 1))
    offset_x = offset[0]
    offset_y = offset[1]
    spacing_x = spacing[0]
    spacing_y = spacing[1]
    input_array = np.zeros_like(image_array_trans)
    known_array = np.zeros_like(image_array_trans)

    # Starting with a Zero-array and updating the wanted pixel to the specific value of image array
    # Starting with a Zero-array and updating the wanted pixel to 1
    j = 0
    while j < len(image_array_trans):
        i = offset_y
        while i < len(image_array_trans[0, ::, ::]):
            input_array[j, i, offset_x::spacing_x] = image_array_trans[j, i, offset_x::spacing_x]
            known_array[j, i, offset_x::spacing_x] = 1
            i += spacing_y
        j += 1

    # getting target array with help of the known array
    target_array = image_array_trans[known_array < 1]

    # check if more than 144 known pixels
    if np.sum(known_array)/3 < 144:
        raise ValueError

    return input_array, known_array, target_array


if __name__ == "__main__":
    # For testing...
    arr = np.array(range(62208)).reshape(144, 144, -1)
    # arr = np.transpose(arr, (2, 0, 1))
    # print(len(arr))

    print(ex4(arr, offset=(1, 1), spacing=(2, 2))[0].shape)
