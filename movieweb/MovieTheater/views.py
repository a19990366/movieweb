from django.shortcuts import render



def MovieTheater(request):
    '''
    Render the MovieTheater page
    '''
    return render(request, 'MovieTheater/MovieTheater.html')