from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Treinador, Nadador, EstiloDeTreino, Treino

@admin.register(Treinador)
class TreinadorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Nadador)
class NadadorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(EstiloDeTreino)
class EstiloDeTreinoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hora', 'treinador')
    list_filter = ('treinador', 'hora')
    search_fields = ('nome',)
    filter_horizontal = ('nadadores',)  # melhora a UI para campos ManyToMany