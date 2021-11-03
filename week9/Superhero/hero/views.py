from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Superhero
from django.urls import reverse_lazy



class showMainView(ListView):
    model = Superhero
    template_name = 'show_main_view.html'

class showListView(ListView):
    model = Superhero
    template_name = 'show_list_view.html'

class showListDetailView(TemplateView):
    model = Superhero
    template_name = 'show_list_detail_view.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = Superhero.objects.get(pk=hero_id)
        return {'hero': hero}

class showDetailView(ListView):
    model = Superhero
    template_name = 'show_detail_view.html'

class showCreateView(CreateView):
    model = Superhero
    template_name = 'show_create_view.html'
    fields = ["name", "description", "identity", "strength", "weakness", "image"]

class showUpdateView(UpdateView):
    model = Superhero
    template_name = 'show_update_view.html'
    fields = ["name", "description", "identity", "strength", "weakness", "image"]

class showDeleteView(DeleteView):
    model = Superhero
    template_name = 'show_delete_view.html'
    success_url = reverse_lazy('hero_list')



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

