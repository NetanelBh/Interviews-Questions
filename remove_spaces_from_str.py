def remove_spaces(string):
    res = ''
    for char in string:
        if char != " ":
            res += char

    return res


if __name__ == "__main__":
    print(remove_spaces("bla dlkfj  slkdfj   slkdjfsldfkj sdfj lskdjf lskdjf"))
