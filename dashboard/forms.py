from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class formsCheckNumber(forms.Form):
    number_field = forms.IntegerField()

# Tama
from .models import Application, KodeBankDummy, CleansingBank, ReturBankLain

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['group_parent', 'name_app', 'ip_app']


class KodeBankForm(forms.ModelForm):
    class Meta:
        model = KodeBankDummy
        fields = ['sandi_kliring', 'nama_bank', 'BIC']  # Sesuaikan dengan field yang ingin Anda tampilkan dalam form

class CleansingBankForm(forms.ModelForm):
    class Meta:
        model = CleansingBank
        fields = ['ISPROCESS', 'ISGENERATE', 'ISCHANGE', 'TRX_TYPE', 'NO', 'SOR_POTONG', 'MNT_STATUS']  
        
class ReturBankLainForm(forms.ModelForm):
    class Meta:
        model = ReturBankLain
        fields = ['SOR', 'TRX_STATUS', 'STATUS_PROCESS']  
#anggitia