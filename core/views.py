from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView

from core.models import TableReservation, Menu, MenuCategory
from .forms import ReservationForm


class TableReservationView(LoginRequiredMixin, CreateView):
    model = TableReservation
    form_class = ReservationForm
    template_name = 'core/reservation.html'
    success_message = "Your Reservation Send to Restaurant, You will get a email if reservation approved. "

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        return render(self.request, 'core/success.html')
        # return super().form_valid(form)


def check_time(request):
    form = ReservationForm(request.GET)
    context = {
        'field': as_crispy_field(form['start_time']),
        'valid': not form['start_time'].errors
    }
    return render(request, 'partials/field.html', context)


class MenuListView(ListView):
    model = MenuCategory
    context_object_name = 'menu'
    template_name = 'core/menu.html'
    queryset =  MenuCategory.objects.all()
