import collections
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    result ={}
    print(type(strs),type(strs[0]))
    i = 0
    while(i<len(strs)):
        key = get_key(strs[i])
        try:
            result[key].append(strs[i])
        except:
            result[key] = [strs[i]]
        i += 1

    return result.values()


def get_key(ele):
    result = [0]*26
    for i in ele:
        result[ord(i)-97] = result[ord(i)-97]+1
    return tuple(result)



print(group_anagrams(["cab","tin","pew","lil","duh","may","ill","buy","bar","max","doc"]))