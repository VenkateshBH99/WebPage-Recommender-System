from django import forms
from recommand.models import Predictions

class Predict_Form(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = ('WebPage1','WebPage2','WebPage3','WebPage4','WebPage5','WebPage6')
        widgets = {'WebPage1': forms.Select(attrs={'class': 'form-control'}),
                   'WebPage2': forms.Select(attrs={'class': 'form-control'}),
                   'WebPage3': forms.Select(attrs={'class': 'form-control'}),
                   'WebPage4':forms.Select(attrs={'class': 'form-control'}),
                   'WebPage5':forms.Select(attrs={'class': 'form-control'}),
                   'WebPage6':forms.Select(attrs={'class': 'form-control'}),
                   }
