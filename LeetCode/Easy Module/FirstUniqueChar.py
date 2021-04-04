def firstUniqChar(s) -> int:
    temp = {}
    for i in range(len(s)):
        try:
            v = temp[s[i]]
            temp[s[i]] = -1
        except:
            temp[s[i]] = i

    for i, j in temp.items():
        if j != -1:
            return j
    return -1


print(firstUniqChar('dsgghfydgfcvxfdsfdxffxfd'))
