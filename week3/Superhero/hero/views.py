from django.views.generic import TemplateView

class MainView(TemplateView):
    template_name = 'main.html'

class HulkView(TemplateView):
    template_name = 'hulk.html'

class IronmanView(TemplateView):
    template_name = "ironman.html"
    
class BatmanView(TemplateView):
    template_name = "batman.html"
    