from django.contrib import admin
from recommand.models import Predictions
from django import forms

class Prediction(admin.ModelAdmin):
    list_display=('WebPage1','WebPage2','WebPage3','WebPage4','WebPage5','WebPage6')
admin.site.register(Predictions,Prediction)
# Register your models here.
