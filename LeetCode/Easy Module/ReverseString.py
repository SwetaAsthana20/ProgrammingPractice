def reverseString(s) -> None:
    size = len(s) // 2
    i = 0

    while i < size:
        s[i], s[-1 * (i + 1)] = s[-1 * (i + 1)], s[i]

        i += 1
    return s


print(reverseString(['s', 'w', 'e', 't', 'a']))