"""
To return a string of 3 digit number:

"""

number = str(input("Enter a 3 digit No"))

number_dict = {
    '1': ['One hundred ', 'Ten', 'One'],
    '2': ['Two hundred ', 'Twenty', 'Two'],
    '3': ['Three hundred ', 'Thirty', 'Three'],
    '4': ['Four hundred ', 'Forty', 'Four'],
    '5': ['Five hundred ', 'Fifty', 'Five'],
    '6': ['Six hundred ', 'Sixty', 'Six'],
    '7': ['Seven hundred ', 'Seventy', 'Seven'],
    '8': ['Eight hundred ', 'Eighty', 'Eight'],
    '9': ['Nine hundred ', 'Ninety', 'Nine'],

}

keys_list = list(number_dict.keys())
values_list = list(number_dict.values())

answer = ''
for i, j in enumerate(number):
    if i == 0:
        if j[0] in keys_list:
            answer += number_dict.get(j[0])[0]
    if i == 1:
        if j[1] in keys_list:
            answer += number_dict.get(j[1])[1]
    if i == 2:
        if j[2] in keys_list:
            answer += number_dict.get(j[2])[2]


print(answer)
