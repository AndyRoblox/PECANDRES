import json
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Score

@xframe_options_exempt
@ensure_csrf_cookie
def game_view(request):
    return render(request, 'game/juego.html')

class ScoresAPIView(View):
    def get(self, request):
        size = getattr(settings, 'LEADERBOARD_SIZE', 20)
        scores = Score.objects.values('id','name','score','created_at')[:size]
        data = [{'id':s['id'],'name':s['name'],'score':s['score'],
                 'created_at':s['created_at'].isoformat()} for s in scores]
        return JsonResponse(data, safe=False)

    def post(self, request):
        body  = json.loads(request.body)
        name  = str(body.get('name','')).strip()[:32]
        score = int(body.get('score', 0))
        entry = Score.objects.create(name=name, score=score)
        return JsonResponse({'id':entry.id,'name':entry.name,
                             'score':entry.score}, status=201)