def generate_parenthesis(nums):
    if nums > 1:
        result = []
        def get_parenthesis(num, temp):
            if num == 0  and len(temp) == nums*2:
                result.append(temp)
                return
            if num - 1 >= 0:
                get_parenthesis(num-1, temp+")")
            if nums * 2 - len(temp) >= num:
                get_parenthesis(num+1, temp+"(")


        get_parenthesis(1, '(')
        return result
    else:
        return ["()"]



print(generate_parenthesis(3))