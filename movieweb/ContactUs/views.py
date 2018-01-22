from django.shortcuts import render, redirect
from django.contrib import messages


from ContactUs.forms import ContactUsForm







def ContactUs(request):
    '''
    Render the ContactUs page
    '''
    template = 'ContactUs/ContactUs.html'
    if request.method == 'GET':
        return render(request, template, {'ContactUsForm':ContactUsForm()})
    # POST
    contactusform = ContactUsForm(request.POST)
    if not contactusform.is_valid():
        return render(request, template, {'contactusform':contactusform})
    contactusform.save()
    messages.success(request, '訊息傳送成功')
    return redirect('main:main')