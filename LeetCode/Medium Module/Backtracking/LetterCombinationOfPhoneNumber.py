mapping = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}


def letter_combination(num):
    result = []

    def make_combinations(i, cur):
        if i == len(num):
            if len(cur) > 0:
                result.append(cur)
            return
        for ch in mapping[num[i]]:
            # cur.append(ch)
            make_combinations(i + 1, cur + ch)
            # cur.pop()

    make_combinations(0, '')

    return result


print(letter_combination("234"))
