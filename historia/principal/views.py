from django.shortcuts import render

def inicio(request):
    """Página principal del proyecto PEC - Conectando Conciencias"""
    context = {
        'titulo': 'Conectando Conciencias',
        'slogan': 'Decide tu futuro: Estás a tiempo',
        'video_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ'
    }
    return render(request, 'principal/index.html', context)


def juego(request):
    return render(request, 'principal/juego.html')

def quiz(request):
    return render(request, 'principal/quiz.html')