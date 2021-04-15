from django import forms

from .models import Recruit, Apply, Comp

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ('name', 'Description')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'Description' : forms.Textarea(attrs={'class':'form-control'}),
        }


class ApplyFrom(forms.ModelForm):
    FullName = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'add your name..'}))
    experience = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'add your years of experience..'}))

    class Meta:
        model = Apply
        fields = ('FullName', 'experience', 'Cv')


   
class skillsFrom(forms.ModelForm):
    class Meta:
        model = Comp
        fields = ('name', 'importance') 

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'importance' : forms.TextInput(attrs={'class':'form-control'})
        }