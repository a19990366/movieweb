from django import forms
from ContactUs.models import ContactMe


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label='姓名', max_length=128)
    email = forms.CharField(label='e-mail',max_length=128)
    phonenumber = forms.CharField(label='電話',max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    
    class Meta:
        model = ContactMe
        fields = ['name', 'email','phonenumber','content']