from django.contrib import admin
from Movie.models import MovieName, Ticket, Person


admin.site.register(MovieName)
admin.site.register(Ticket)
admin.site.register(Person)