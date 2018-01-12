from django.shortcuts import render



def ContactUs(request):
    '''
    Render the ContactUs page
    '''
    return render(request, 'ContactUs/ContactUs.html')