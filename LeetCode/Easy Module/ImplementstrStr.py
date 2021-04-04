def implementStr(haystack: str, needle: str) -> int:
    len_s1 = len(haystack)
    len_s2 = len(needle)
    for i in range(len_s1 - len_s2 + 1):
        substring = haystack[i:i + len_s2]
        if substring == needle:
            return i
    return -1


print(implementStr(haystack="hello", needle="ll"))
