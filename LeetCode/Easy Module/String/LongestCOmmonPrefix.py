from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    result = ''
    if strs:
        mini_str = min(strs, key=len)
        flag = True
        if mini_str:
            for i in range(len(mini_str)):
                for j in strs:
                    if j[i] != mini_str[i]:
                        flag = False
                        break
                if flag:
                    result += mini_str[i]
    return result


print(longestCommonPrefix(["flower","flow","flight"]))
