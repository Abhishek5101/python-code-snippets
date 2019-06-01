import csv


with open('practice_csv_file.csv') as csvfile:
    readCSV = csv.DictReader(csvfile, delimiter=",")

    with open('new_practice.csv', 'w') as new_file:
        fieldnames = [1, ]

    for line in readCSV:
        print(line)
