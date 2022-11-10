from django import forms   
class MLForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    v1 = forms.CharField(max_length=20)
    v2 = forms.CharField(max_length=20)
    v3 = forms.CharField(max_length=20)
    v4 = forms.CharField(max_length=20)
    #All my attributes here