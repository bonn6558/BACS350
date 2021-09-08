from django.urls import path
from hero.views import HulkView, IronmanView, BatmanView

urlpatterns = [
    path('hulk', HulkView.as_view()),
    path('ironman', IronmanView.as_view()),
    path('batman', BatmanView.as_view()),
]