def happy_number(num):
    def get_num(num):
        result = 0
        while num:
            result += (num%10)**2
            num = num//10
        return result

    cache = [num]
    while num:
        num = get_num(num)
        if num==1:
            return True
        elif num in cache:
            return False
        cache.append(num)


print(happy_number(100))