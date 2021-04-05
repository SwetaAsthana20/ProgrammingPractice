def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def checkAangram(s, t):
    if len(s) != len(t):
        return False
    check = [0] * 26
    for i in range(len(s)):
        check[ord(s[i]) - ord('a')] += 1
        check[ord(t[i]) - ord('a')] -= 1

    for i in check:
        if i != 0:
            return False
    return True


print(isAnagram(s="anagram", t="nagaram"))
print(checkAangram(s="anagram", t="nagaram"))
