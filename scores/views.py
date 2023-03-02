from django.shortcuts import render
from .models import Fixture

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def fixtures(request):
    fixtures = Fixture.objects.all()
    # проверяем, закончились ли все матчи
    all_completed = all(f.game_finished for f in fixtures)

    context = {
        'fixtures': fixtures,
        'all_completed': all_completed
    }
    if request.htmx:
        if all_completed:
            response = render(request, 'partials/fixturelist.html', context)
            response['HX-Refresh'] = "true"
            return response
        return render(request, 'partials/fixturelist.html', context)
    else:
        return render(request, 'fixtures.html', context)