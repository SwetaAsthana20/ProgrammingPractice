def isPalindrome(s: str) -> bool:
    size = len(s)
    if size > 1:
        s = s.lower()
        s = list(filter(str.isalnum, s))
        return bool(s == s[::-1])
    return True


print(isPalindrome("race a car"))