from django import forms
from .models import jobforms
from .models import contact




class job(forms.ModelForm):
    
    class Meta:
        model = jobforms
        fields = ("Name","Phoneno","email","resume","created_at")


class cont(forms.ModelForm):

    class Meta:
        model =contact
        fields = ("name","email","mesg")      





    
 



