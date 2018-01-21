from django import forms
from Movie.models import Person, Ticket


# 預訂車票填寫信息Form
class TicketForm(forms.Form):

    name = forms.CharField(label='名稱', max_length=10, error_messages={'required': '請填寫您的名字',})
    phone_number = forms.CharField(label='電話號碼', min_length=10, max_length=10,error_messages={'required': '請輸入手機號碼'})
    ticket_num = forms.CharField(label='電影編號', max_length=10, error_messages={'required': '電影票編號輸入錯誤'})



# 查詢信息填寫Form
class PersonForm(forms.Form):
    name = forms.CharField(label='name', max_length=10, error_messages={'required': '請填寫您的名字'})
    phone_number = forms.CharField(label='phone_number', min_length=10, max_length=10,error_messages={'required': '請輸入手機號碼'})