from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from core.models import TableReservation
from .forms import ReservationForm


class TableReservationView(LoginRequiredMixin, CreateView):
    model = TableReservation
    form_class = ReservationForm
    template_name = 'core/reservation.html'
    # error_message = ' check fields below.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('landing-page')
        # return super().form_valid(form)
