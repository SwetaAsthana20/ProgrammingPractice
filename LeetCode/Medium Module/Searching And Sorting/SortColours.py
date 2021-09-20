def sort_colours(arr):
    index, zero_pointer, two_pointer= 0,0,len(arr)-1

    while(index<=two_pointer):
        if arr[index] == 0:
            arr[index], arr[zero_pointer] = arr[zero_pointer], arr[index]
            zero_pointer += 1
            #index += 1
        elif arr[index] == 2:
            arr[index], arr[two_pointer] = arr[two_pointer], arr[index]
            two_pointer -= 1
        else:
            index += 1

    return arr


print(sort_colours([2,0,1]))
