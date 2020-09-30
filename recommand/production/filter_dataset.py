import csv

f = open("msnbc990928.txt","r")
i = 0
dataset = []
for line in f:
	l = line.split(" ")
	if len(l) == 8 and i <= 5000:
		i = i+1
		l.pop()
		dataset.append(l)
		print(l)

with open('dataset.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(dataset)