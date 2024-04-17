from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CleansingBank, ReturBankLain

class CleansingBankForm(forms.ModelForm):
    class Meta:
        model = CleansingBank
        fields = ['ISPROCESS', 'ISGENERATE', 'ISCHANGE', 'TRX_TYPE', 'NO', 'SOR_POTONG', 'MNT_STATUS']  
        
class ReturBankLainForm(forms.ModelForm):
    class Meta:
        model = ReturBankLain
        fields = ['SOR', 'TRX_STATUS', 'STATUS_PROCESS']  
#anggitia