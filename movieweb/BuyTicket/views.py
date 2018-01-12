from django.shortcuts import render



def BuyTicket(request):
    '''
    Render the BuyTicket page
    '''
    return render(request, 'BuyTicket/BuyTicket.html')