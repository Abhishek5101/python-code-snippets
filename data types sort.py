#
#
# # I want to take out items in the list that are not of the type Integer
# my_list = [1,2,True,"sup",]
# new_list = []
#
# for item in my_list:
#     if type(item) == int:
#         new_list.append(item)
#
# print(new_list)
#
# # But apparently all it does is take out the first element from the list

def first_and_last_4(iterable):
    return iterable[:4], iterable[-1:-5:-1]
