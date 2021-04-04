def countAndSay(n: int) -> str:
    temp = "11"

    if n > 2:
        for j in range(n - 2):
            count = 1
            result = ""
            i = 0
            while i <= len(temp) - 1:
                if i == len(temp) - 1 or temp[i] != temp[i + 1]:
                    result += str(count) + str(temp[i])
                    count = 1
                else:
                    count += 1
                i += 1
            temp = result

    elif n == 1:
        temp = 1

    return str(temp)

print(countAndSay(4))