def find_index(array, element):
    index = 0
    for i in array:
        if i == element:
            print(index)
        else:
            index += 1


# find_index([1,2,3,4], 4)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    sorted_array = array
    print(sorted_array)


bubble_sort([20, 30, 40, 90, 50, 60, 70, 80, 100, 111, 110])
