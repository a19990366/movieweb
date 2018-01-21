from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


from Movie.models import MovieName, Person, Ticket
from Movie.forms import TicketForm, PersonForm




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
    MovieID = str(Movie.id)
    context = {
        'Movie': Movie,
        'MovieID':MovieID,
    }
    return render(request, 'Movie/MovieIntroduction.html', context)




def MovieEquipment(request):
    '''
    Render the MovieEquipment page
    '''
    return render(request, 'Movie/MovieEquipment.html')




@login_required
def detailview(request):
    '''
    Render the BuyTicket page
    '''
    tickets = Ticket.objects.all()
    persons = Person.objects.all()
    ticket_form = TicketForm()
    person_form = PersonForm()
    content = {
        'tickets': tickets,
        'persons': persons,
        'ticket_form': ticket_form,
        'person_form': person_form,
    }
    return render(request, 'Movie/order_system.html', context=content)



@login_required
def Order(request):
    
    if request.method == 'POST':
        
        ticket_form = TicketForm(request.POST)
        tickets = Ticket.objects.all()
        persons = Person.objects.all()
        person_form = PersonForm()

        content = {
            'tickets': tickets,
            'persons': persons,
            'ticket_form': ticket_form,
            'person_form': person_form,
            'order_message': ''
        }
        
        if ticket_form.is_valid():

            ticket = get_object_or_404(Ticket, num=request.POST['ticket_num'])
            
            person = Person.objects.create() if not Person.objects.filter(name=request.POST['name']) \
                else Person.objects.get(name=request.POST['name'])
            
        
            if person.ticket_name == ticket.num:
                message = '您已訂過此票！'
            else:
                if ticket.seats >= 1:
                    message = '訂票成功！'
                    ticket.seats -= 1
                    ticket.save()
                    person.name = request.POST['name']
                    person.phone_number = request.POST['phone_number']
                    person.ticket_time = ticket.time
                    person.ticket_name = request.POST['ticket_num']
                    person.save()
                else:
                    message = '座位已滿！'
                    person.delete()

            content['order_message'] = message

        return render(request, 'Movie/order_system.html', context=content)

    else:

        return HttpResponseRedirect(reverse(Order))




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




