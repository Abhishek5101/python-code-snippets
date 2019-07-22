"""
To return a string of 3 digit number:

"""

number = str(input("Enter a 3 digit No"))

number_dict = {
    '1': ['One hundred ', 'Ten', ' One'],
    '2': ['Two hundred ', 'Twenty', ' Two'],
    '3': ['Three hundred ', 'Thirty', ' Three'],
    '4': ['Four hundred ', 'Forty', ' Four'],
    '5': ['Five hundred ', 'Fifty', ' Five'],
    '6': ['Six hundred ', 'Sixty', ' Six'],
    '7': ['Seven hundred ', 'Seventy', ' Seven'],
    '8': ['Eight hundred ', 'Eighty', ' Eight'],
    '9': ['Nine hundred ', 'Ninety', ' Nine'],
    '0': ['. ', '.', ' .'],

}

elevens = {
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen',

}

keys_list = list(number_dict.keys())
values_list = list(number_dict.values())

answer = ''
keepgoing = True
for i, j in enumerate(number):
    if i == 0:
        if number[0] in keys_list:
            answer += number_dict.get(number[0])[0]

    if i == 1:
        if number[1:3] in elevens:
            answer += elevens.get(number[1:3])
            keepgoing = False
        else:
            answer += number_dict.get(number[1])[1]

    if i == 2 and keepgoing:
        if number[2] in keys_list:
            answer += number_dict.get(number[2])[2]


print(answer)
