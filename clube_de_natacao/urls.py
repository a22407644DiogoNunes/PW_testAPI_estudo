from django.urls import path
from . import views

urlpatterns = [
    path('nadadores/', views.nadadores_view, name='nadadores')
]