def days_left(day, month, year):
    # res = 0
    # Option1: sum all the days per month
    # months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #
    # # Check first if is a leap year
    # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    #     res += 1
    #
    # for i in range(month - 1):
    #     res += months[i]
    #
    # res += day
    # return res

    # Option2: create an array with accumulated days sum
    months = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

    res = months[month - 2]
    res += day

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        res += 1

    return res


if __name__ == "__main__":
    print(days_left(31, 7, 2024))
