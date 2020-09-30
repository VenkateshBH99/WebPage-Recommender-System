import csv
import random
import numpy as np
import math
import pandas as pd

file = open("dataset.csv")
data = csv.reader(file,delimiter=",")
data = list(data)
datax = list(data)

data = [x[:-1] for x in data[1:]]
datax = [x[:-1] for x in datax[1:]]

data = np.asarray(data,dtype=float)
data
centre = []

def matriksmakee():
    matriksu = list()
    for i in range(len(data)):
        randomnumber = [random.random() for x in range(c)]
        findd = sum(randomnumber)
        temp = list()
        for x in randomnumber:
            temp.append(round(x/findd,3))
        matriksu.append(temp)
    return matriksu

def centroid(makee):
    xraised = []
    finddcentroid = []
    centroid = []
    for x in range(len(data)):
        raised = []
        for y in range(c):
            cie = math.pow(makee[x][y],w)
            raised.append(cie)
        xraised.append(raised) 
    for x in range(c):
        sumz = 0
        for y in range(len(data)):
            sumz += xraised[y][x]
        finddcentroid.append(sumz)
    for i in range(c):
        temp = []
        for x in range(len(data[0])):
            sum_u = 0
            for y in range(len(data)):
                sum_u += (xraised[y][i]*data[y][x])/(finddcentroid[i])
            temp.append(round(sum_u,4))
        centroid.append(temp)
    return centroid

def objective(centroid,makee):
    obj = 0
    dist = []
    xraised = []
    for x in range(len(data)):
        raised = []
        for y in range(c):
            cie = math.pow(makee[x][y],w)
            raised.append(cie)
        xraised.append(raised)
    for x in range(len(data)):
        temp = []
        for y in range(c):
            sum_z = 0
            for i in range(len(data[0])):
                sum_z += math.pow(data[x][i]-centroid[y][i],2)
            temp.append(sum_z)
        dist.append(temp)
    for x in range(len(data)):
        for y in range(c):
            obj += dist[x][y]*xraised[x][y]
    return obj

def updateMatriks(makee,centroid):
    dist = []
    for x in range(len(data)):
        temp = []
        for y in range(c):
            sum_z = 0
            for i in range(len(data[0])):
                sum_z += math.pow(data[x][i]-centroid[y][i],2)
            temp.append(round(math.sqrt(sum_z),4))
        dist.append(temp)
    distraised = []
    for i in range(len(dist)):
        temp = []
        for j in range(len(dist[0])):
            x=1/(dist[i][j]**2)
            temp.append(x)
        distraised.append(temp)
    findd = []
    pop = 0
    for i in range(len(distraised)):
        for j in range(len(distraised[0])):
            pop += distraised[i][j]
        findd.append(pop)
        pop = 0
    updatematrix = []
    for i in range(len(distraised)):
        temp = []
        for j in range(len(distraised[0])):
            x = distraised[i][j]/findd[i]
            temp.append(x)
        updatematrix.append(temp)
    return updatematrix

def findcluster(u):
    cluster = []
    for x in u:
        cluster.append(np.argmax(x)+1)
    return cluster

c=100
w=2
n=20
wew = matriksmakee()

#result = [0 for i in range(20)]
#for qr in range(20):

membership = wew
o1= 0
o2 = 999
e = 0.1
i = 0
maxiter = 100
while abs(o1-o2) > e:
    centroidd = centroid(membership)
    o2 = o1
    o1 = objective(centroidd,membership)
    membership = updateMatriks(membership,centroidd)
cluster = findcluster(membership)

file.close()

file1 = open("dataset.csv")
data1 = csv.reader(file1,delimiter=",")
data1 = list(data1)

wrong = 0
correct = 0

for m in range(1,len(data1)):
    user = data1[m]
    for i in range(len(user)):
        user[i]=int(user[i])
    Weight = [i for i in range(n,0,-1)]
    top_cluster = []
    for i in range(c):
        val = 0
        for j in range(6):
            val = val+(centroidd[i][j]-user[j])**2
        temp = [val,i]
        top_cluster.append(temp)
    top_cluster.sort(key = lambda x: x[0])
    top_n_cluster = []
    for i in range(n):
        top_n_cluster.append(top_cluster[i][1])    
    
    for i in range(len(cluster)):
        datax[i].append(cluster[i])
    
    similar_user = [0 for i in range(17)]
    target_user = [0 for i in range(17)]
    probability = [0 for i in range(17)]
    size_user = 0
    
    for i in range(6):
        target_user[int(user[i])-1] = target_user[int(user[i])-1]+1
    
    for i in range(n):
        for j in range(len(datax)):
            if(top_n_cluster[i] == datax[j][-1]):
                size_user = size_user+6
                weight = Weight[i]
                for k in range(6):
                    similar_user[int(datax[j][k])-1] = similar_user[int(datax[j][k])-1]+weight
    for i in range(17):
        probability[i] = (target_user[i]+0.01*similar_user[i])/size_user
    
    recommendation = 1+probability.index(max(probability))
    if data1[m][6] == recommendation:
        correct = correct+1
    else:
        wrong = wrong+1
    accuracy = correct/(wrong+correct)*100

print("accuracy is ",accuracy)
#result[qr] = accuracy
#print("accuracy is "max(result))






















