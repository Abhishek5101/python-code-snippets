# def sum_all_nums(list):
#     answer = 0
#
#     for num in list:
#         try:
#             answer += num
#             print(answer)
#         except NameError:
#             print("wring value")
#
#
# sum_all_nums([1,2,3, False])

#
# def largest_num(list):
#     largest = 0
#     for num in list:
#         if num > largest:
#             largest = num
#     print(largest)
#     return largest
#
#
# largest_num([2, 3, 58, 1])
#

def replace(list1, list2):
    list1[-1] = list2
    print(list1)


replace([1,2,3,4,5], [67,78])
