import csv

output = open('myCSV.csv', mode = 'w')

mywriter = csv.writer(output)

header = ['name','age']
mywriter.writerow(header)

data = ['Bob Johnson','50']

mywriter.writerow(data)

output.close()
