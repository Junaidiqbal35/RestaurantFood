from django.urls import path
from django.views.generic import TemplateView
from .views import TableReservationView
urlpatterns = [
    path('', TemplateView.as_view(template_name="core/landing_page.html"), name='landing-page'),
    path('table/reservation/', TableReservationView.as_view(), name='table-reservation'),
]