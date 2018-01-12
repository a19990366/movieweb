from django.shortcuts import render



def MovieEquipment(request):
    '''
    Render the MovieEquipment page
    '''
    return render(request, 'MovieEquipment/MovieEquipment.html')