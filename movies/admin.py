from django.contrib import admin

from movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'language', 'rating')


admin.site.register(Movie, MovieAdmin)
