from django.contrib import admin

from movies.models import Movie, Actor, Director


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'language', 'rating')
    list_filter = ('language', )


class BasePersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender')
    list_filter = ('gender', )


class ActorAdmin(BasePersonAdmin):
    pass


class DirectorAdmin(BasePersonAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
