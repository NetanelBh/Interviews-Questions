def tribonacci(n):
    n1 = 0
    n2 = n3 = 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 2

    for num in range(3, n + 1):
        summ = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = summ

    return n3


if __name__ == '__main__':
    print(tribonacci(4))
