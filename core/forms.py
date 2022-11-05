from django import forms
from django.utils import timezone

from .models import TableReservation, Table
import datetime as dt

from .utils import check_free_time

HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00 pm'.format(x)) for x in range(1, 13)]


class ReservationForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.Select(choices=HOUR_CHOICES))

    def __init__(self, *args, **kwargs):  # note the additional user param
        self.table = Table.objects.filter(available=True)
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['table'].queryset = self.table
        # self.fields['start_time'] = self.available_slot

    class Meta:
        model = TableReservation
        fields = ['full_name', 'table', 'booking_date', 'start_time']

    def clean(self):
        super().clean()
        start_time = self.cleaned_data['start_time']
        booking_date = self.cleaned_data['booking_date']
        print(start_time.hour)
        today_bookings = TableReservation.objects.filter(booking_date=booking_date)
        today_time_slot = today_bookings.values('start_time__hour')
        today_time_slot_list = [h['start_time__hour'] for h in list(today_time_slot)]
        all_time_slot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        available_slot = check_free_time(all_time_slot, today_time_slot_list)

        if available_slot:
            if start_time.hour not in available_slot:
                # if `subscribe` is checked but there is no email we raise an error
                message = f"Requested slot is already booked, please choose another time in {available_slot} pm."
                print(message)
                raise forms.ValidationError(message)

        else:  # The list is empty, all slot are taken
            message = "The are not available slot for this booking today."
            raise forms.ValidationError(message)

# 'hx-get': reverse_lazy('check-username'),
#                'hx-target': '#div_id_username',
#                'hx-trigger': 'keyup[target.value.length > 3]
