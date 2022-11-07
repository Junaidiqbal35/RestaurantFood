from django.urls import path
from django.views.generic import TemplateView
from .views import TableReservationView, MenuListView
urlpatterns = [
    path('', TemplateView.as_view(template_name="core/landing_page.html"), name='landing-page'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('table/reservation/', TableReservationView.as_view(), name='table-reservation'),
]
