from django import forms

class Usersform(forms.Form):
    num1=forms.CharField(label='Value1',required=False,widget=forms.Textarea(attrs={'class':"form-control"}))
    num2=forms.CharField(label='Value2',widget=forms.Textarea(attrs={'class':"form-control"}))
    email=forms.EmailField()
