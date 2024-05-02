# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also
# exists in the array

def largest_positive(arr):
    hashmap = dict()
    largest = -1

    for num in arr:
        # If we found the opposite number
        if hashmap.get(num * -1) is not None and hashmap.get(num * -1) == 0:
            # If num smaller than 0, will add it as value
            if num < 0:
                hashmap[num * -1] = num
            # If num greater than 0, will make it the key, and -num will be the value
            else:
                hashmap[num] = num * -1
        elif hashmap.get(num * -1) is None and hashmap.get(num) is None:
            hashmap[num] = 0

    for key in hashmap:
        if hashmap.get(key):
            if key > largest:
                largest = key

    return largest


if __name__ == '__main__':
    array = [-23, 29, -35, -9, -38, 11, 24, -16, 50, -1, -10, 6, -33, 14, -3, -19, 13, -27, -8, 6, -4, 40, 33,
           21, -12, -2, -26, 17, 35, -45,
           -15, -40, -12, 21, -36, -30, -17, -2, 19, -33, 26, -39, -6, -31, 31, 16, 36, -24, 43, -32, 5, 34,
           -50, -1, 25, 28, 49, 17, -36, 36,
           -44, -5, -20, -11, -36, -27, 40, -29, 34, 33, 29, 41, -8, 43, 8, -30, -8, 50, -45, -19]
    print(largest_positive(array))
