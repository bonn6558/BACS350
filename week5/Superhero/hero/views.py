from django.views.generic import ListView, TemplateView
from .models import Superhero


class MainView(TemplateView):
    template_name = 'main.html'


class HeroView(ListView):
    model = Superhero
    template_name = 'hero.html'


class HeroDetailView(TemplateView):
    model = Superhero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Superhero.objects.get(pk=hero_id)
        return {'hero': hero}

