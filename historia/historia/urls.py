from django.contrib import admin
from django.urls import path, include
from game.views import ScoresAPIView 
from django.contrib import admin
from django.urls import path, include
from principal.views import inicio, quiz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('juego/', include('game.urls')), 
    path('api/scores/', ScoresAPIView.as_view()),  
    path('', inicio, name='inicio'),
    path('quiz/', quiz, name='quiz'),
]



