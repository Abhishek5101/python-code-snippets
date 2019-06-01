def dog_age(age):
    if age < 2:
        answer = age * 10.5
        print("Age in Human time: {}".format(answer))
    elif age > 2:
        answer = 2 * 10.5 + 4*age
        print("Age in Human Time : {}".format(answer))


dog_age(13)
