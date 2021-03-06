# @Time    : 2019/4/21 0:34
# @Author  : Noah
# @File    : merge_sort.py
# @Software: PyCharm
# @description: python -m doctest -v merge_sort.py

def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    # >>> merge_sort([0, 5, 3, 2, 2])
    # [0, 2, 2, 3, 5]
    # >>> merge_sort([])
    # []
    # >>> merge_sort([-2, -5, -45])
    # [-45, -5, -2]
    """
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])

        i, j, k = 0, 0, 0
        left_length = len(left_half)
        right_length = len(right_half)

        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1

    return collection


if __name__ == "__main__":
    print(merge_sort([12, 9, 20, 18, 3, 1, 13, 20]))
