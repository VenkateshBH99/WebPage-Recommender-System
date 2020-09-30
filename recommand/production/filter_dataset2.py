import csv

f = open("msnbc990928.txt","r")
i = 5000
dataset = []
for line in f:
	l = line.split(" ")
	if len(l) == 8:
		i = i+1
		if i <= 7000:
			l.pop()
			dataset.append(l)

with open('testset.csv','w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(dataset)