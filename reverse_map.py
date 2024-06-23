import numpy as np


def reverse_map(arr):
    # for inner_arr in arr:
    #     inner_arr.reverse()

    return np.fliplr(arr)

    # for n in array:
    #     left = 0
    #     right = len(n) - 1
    #     while left < right:
    #         temp = n[left]
    #         n[left] = n[right]
    #         n[right] = temp
    #
    #         left += 1
    #         right -= 1


if __name__ == "__main__":
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    # Example1
    # reverse_map(array)

    # Example2
    print(reverse_map(array))

    # Example3
    # reverse_map(array)
    # print(array)
