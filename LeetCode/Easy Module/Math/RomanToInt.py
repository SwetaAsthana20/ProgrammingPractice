def romanToInt(s: str) -> int:
    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = list(s)
    result = 0
    prev = romanMap[s[-1]]
    for i in range(len(s) - 1, -1, -1):
        if prev <= romanMap[s[i]]:
            result += romanMap[s[i]]
        else:
            result -= romanMap[s[i]]
        prev = romanMap[s[i]]

    return result


print(romanToInt('LVIII'))