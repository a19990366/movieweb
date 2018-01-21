from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from Movie.models import MovieName, Person, Ticket
from Movie.forms import TicketForm, PersonForm
from datetime import datetime




def NEWS(request):
    '''
    Render the NEWS page
    '''
    Movies = MovieName.objects.all()
    context = {'Movies':Movies}
    return render(request, 'Movie/NEWS.html', context)




def MovieIntroduction(request, articleId):
    '''
    Read an Movie
        1. Get the "Movie" instance using "articleId"; redirect to the 404 page if not found
        2. Render the MovieIntroduction template with the Movie instance and its
           associated comments
    '''
    Movie = get_object_or_404(MovieName, id=articleId)
    context = {
        'Movie': Movie,
    }
    return render(request, 'Movie/MovieIntroduction.html', context)




def MovieEquipment(request):
    '''
    Render the MovieEquipment page
    '''
    return render(request, 'Movie/MovieEquipment.html')




@login_required
def OrderTicket(request):
    '''
    Render the BuyTicket page
    '''
    tickets = Ticket.objects.all()
    persons = Person.objects.all()
    ticket_form = TicketForm()
    person_form = PersonForm()
    context = {
        'tickets': tickets,
        'persons': persons,
        'ticket_form': ticket_form,
        'person_form': person_form,
    }
    return render(request, 'Movie/OrderTicket.html', context)



def OrderTickets(request):
    '''
    Render the OrderTickets page
    '''
    return render(request, 'Movie/OrderTickets.html')



@login_required
def MovieLike(request, articleId):
    '''
    Add the user to the 'likes' field:
        1. Get the article; redirect to 404 if not found
        2. If the user does not exist in the "likes" field, add him/her
        3. Finally, call Movie() function to render the article
    '''
    movie = get_object_or_404(MovieName, id=articleId)
    if request.user not in movie.likes.all():
        movie.likes.add(request.user)
    return NEWS(request)




