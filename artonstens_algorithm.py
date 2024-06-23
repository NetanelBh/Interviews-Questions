from math import sqrt


def find_primes(n):
    arr = [True] * (n + 1)
    primes_arr = []

    for p in range(2, int(sqrt(n) + 1)):
        # If arr[p] didn't delete from prev numbers in array, it's prime number
        if arr[p] is True:
            # All multiply numbers are non-prime
            for number in range(p * 2, n + 1, p):
                arr[number] = False

    for i in range(2, n + 1):
        if arr[i] is True:
            primes_arr.append(i)

    return primes_arr


if __name__ == "__main__":
    num = 24
    # Initialize all numbers as prime numbers
    print(find_primes(num))
