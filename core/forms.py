from django import forms
from .models import TableReservation, Table


class ReservationForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))

    def __init__(self, *args, **kwargs):  # note the additional user param
        self.table = Table.objects.filter(available=True)
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['table'].queryset = self.table

    class Meta:
        model = TableReservation
        fields = ['full_name', 'table', 'booking_date', 'start_time']
