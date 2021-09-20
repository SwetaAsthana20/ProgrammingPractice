def longestPalindrome(s: str) -> str:
    i = 0
    end, start = 0, 0
    while i<len(s):
        even = get_palindrome(s, i, i+1)
        odd =  get_palindrome(s, i, i)
        maxlength = max(even, odd)
        if maxlength-1 > end-start:
            start = i - (maxlength-1)//2
            end = i + (maxlength)//2
        i += 1
    return s[start:end+1]


def get_palindrome(s, i, j):
    while(i>=0 and j<len(s) and s[i]==s[j]):
        i -=1
        j +=1
    return j-i-1


print(longestPalindrome('cabbad'))