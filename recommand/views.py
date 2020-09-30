import csv,io
from django.shortcuts import render
from .forms import Predict_Form
from recommand.data_provider import *
from accounts.models import UserProfileInfo
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.urls import reverse
from django.contrib import messages

import numpy
import csv
import random
import math
import os

@login_required(login_url='/')
def PredictRisk(request,pk):
    predicted = False
    predictions={}
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)

        if form.is_valid():
            features = [ form.cleaned_data['WebPage1'], form.cleaned_data['WebPage2'], form.cleaned_data['WebPage3'], form.cleaned_data['WebPage4'], form.cleaned_data['WebPage5'],
            form.cleaned_data['WebPage6']]

            print("Before------",features)
            # standard_scalar = GetStandardScalarForHeart()
            # features = standard_scalar.transform(features)
            print("Hell0-------",features)
            cluster,centroidd,datax=GetAll()


            # predictions = {'SVC': str(SVCClassifier.predict(features)[0]),
            # 'LogisticRegression': str(LogisticRegressionClassifier.predict(features)[0]),
            #  'NaiveBayes': str(NaiveBayesClassifier.predict(features)[0]),
            #  'DecisionTree': str(DecisionTreeClassifier.predict(features)[0]),
            #   'NeuralNetwork': str(NeuralNetworkClassifier.predict(features)[0]),
            #   'KNN': str(KNNClassifier.predict(features)[0]),
            #   }

            user=features
            n=20
            c=100
            w=2
            for i in range(len(user)):
                user[i]=int(user[i])
            #        print(type(user[i]))
            #    print(type(user[1]))
            Weight = [i for i in range(n,0,-1)]
            top_cluster = []
            for i in range(c):
                val = 0
                for j in range(6):
                    val = val+(centroidd[i][j]-user[j])**2
                temp = [val,i]
                top_cluster.append(temp)
            top_cluster.sort(key = lambda x: x[0])
            #    print(top_cluster)
            top_n_cluster = []
            for i in range(n):
                top_n_cluster.append(top_cluster[i][1])
            #    print(top_n_cluster)

            for i in range(len(cluster)):
                datax[i].append(cluster[i])
            #    print(datax)

            similar_user = [0 for i in range(17)]
            target_user = [0 for i in range(17)]
            probability = [0 for i in range(17)]

            for i in range(6):
                target_user[int(user[i])-1] = target_user[int(user[i])-1]+1

            for i in range(n):
                for j in range(len(datax)):
                    if(top_n_cluster[i] == datax[j][-1]):
                        weight = Weight[i]
                        for k in range(6):
                            similar_user[int(datax[j][k])-1] = similar_user[int(datax[j][k])-1]+weight
            #    for i in range(17):
            ##        print(similar_user[i])
            for i in range(17):
                if similar_user[i]>0:
                    probability[i] = target_user[i]/similar_user[i]

            #    print(similar_user)
            #    print(target_user)
            #    print(probability)
            recommendation = 1+probability.index(max(probability))
            #    print(recommendation)
            #    print(data1[m][6]," ",recommendation)
            #    print(recommendation

            print("accuracy is ",recommendation)
            #if user[6] == recommendation:
            #    accuracy = recommendation
            #else:
            #    accuracy = recommendation
            #
            #print("accuracy is ",accuracy)

            pred = form.save(commit=False)

            # l=[predictions['SVC'],predictions['LogisticRegression'],predictions['NaiveBayes'],predictions['DecisionTree'],predictions['NeuralNetwork'],predictions['KNN']]
            # count=l.count('1')

            result=False
            pred.num=recommendation

            # if count>=3:
            #     result=True
            #     pred.num=1
            # else:
            #     pred.num=0

            pred.profile = profile

            pred.save()
            predicted = True

            colors={}

            # if predictions['SVC']=='0':
            #     colors['SVC']="table-success"
            # elif predictions['SVC']=='1':
            #     colors['SVC']="table-danger"

            # if predictions['LogisticRegression']=='0':
            #     colors['LR']="table-success"
            # else:
            #     colors['LR']="table-danger"

            # if predictions['NaiveBayes']=='0':
            #     colors['NB']="table-success"
            # else:
            #     colors['NB']="table-danger"

            # if predictions['DecisionTree']=='0':
            #     colors['DT']="table-success"
            # else:
            #     colors['DT']="table-danger"

            # if predictions['NeuralNetwork']=='0':
            #     colors['NN']="table-success"
            # else:
            #     colors['NN']="table-danger"

            # if predictions['KNN']=='0':
            #     colors['KNN']="table-success"
            # else:
            #     colors['KNN']="table-danger"

            colors['recom']="table-success"

    if predicted:
        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':recommendation,'result':result,'colors':colors})

    else:
        form = Predict_Form()

        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})
