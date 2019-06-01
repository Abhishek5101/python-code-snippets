def snap(data):
    new_list = []
    for i, j in enumerate(data):
        if i % 2 == 0:
            del data[j]
    return data, new_list


snap([1,2,3,4,5,6,7,8,9,10])

