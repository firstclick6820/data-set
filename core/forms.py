from django import forms

from .models import AffiliatePrograms



class AffiliateForm(forms.ModelForm):
    
    class Meta:
        model = AffiliatePrograms
        filed = "__all__"