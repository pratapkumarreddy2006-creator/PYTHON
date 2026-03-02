def l_list():
    ls = [1,2,5,9,6,3,7,10]
    max = 0
    for i in ls:
        if i > max:
            max = i

    return max

print(l_list())