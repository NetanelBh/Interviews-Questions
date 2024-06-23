def biggest_number(n):
    arr = [""] * 10
    res = ""

    while n > 0:
        num = n % 10
        n = int(n / 10)
        arr[num] += str(num)

    for index in range(9, -1, -1):
        res += arr[index]

    return int(res)


if __name__ == "__main__":
    print(biggest_number(2515))
