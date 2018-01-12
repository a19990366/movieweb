from django.shortcuts import render



def MovieIntroduction(request):
    '''
    Render the MovieIntroduction page
    '''
    return render(request, 'MovieIntroduction/MovieIntroduction.html')