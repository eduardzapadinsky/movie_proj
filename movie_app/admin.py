from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'Фільтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низький'),
            ('від 40 до 59', 'Середній'),
            ('від 60 до 79', 'Високий'),
            ('>=80', 'Найвищий'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'від 40 до 59':
            return queryset.filter(rating__gte=40, rating__lte=59)
        if self.value() == 'від 60 до 79':
            return queryset.filter(rating__gte=60, rating__lte=79)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['currency', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['budget']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status', 'year']
    list_editable = ['rating', 'director', 'budget', 'year']
    filter_vertical = ['actors']
    ordering = ['-rating', 'name', 'year']
    list_per_page = 10
    actions = ['set_dollars', 'set_euros']
    search_fields = ['name__startswith', 'rating__startswith']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Краще не дивитись'
        if mov.rating < 70:
            return 'Можна раз подивитись'
        if mov.rating <= 85:
            return 'Добре'
        return 'Супер'

    @admin.action(description='Змінити валюту в долари')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Змінити валюту в євро')
    def set_euros(self, request, qs: QuerySet):
        count_updates = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Було оновлено {count_updates} комірки',
            messages.DEBUG
        )

# Register your models here.
# admin.site.register(Movie, MovieAdmin)
