def fizzBuzz(n: int):
    i = 1
    result = []
    while i <= n:
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 3 == 0:
            result.append('Fizz')
        else:
            result.append(str(i))
        i += 1
    return result


print(fizzBuzz(15))