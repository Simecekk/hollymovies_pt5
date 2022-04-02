from django.contrib import admin

from movies.models import Movie, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'language', 'rating')
    list_filter = ('language', )


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender')
    list_filter = ('gender', )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
