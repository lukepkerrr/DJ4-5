from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    from_city = forms.CharField(
        widget=AjaxInputWidget(
            url='api/city_ajax',
            attrs={'class': 'inline right-margin'}
        ),
        label='Город отправления'
    )
    to_city = forms.CharField(
        widget=AjaxInputWidget(
            url='api/city_ajax',
            attrs={'class': 'inline right-margin'}
        ),
        label='Город прибытия'
    )
    date = forms.DateField(label='Дата')