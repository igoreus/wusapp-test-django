# -*- coding: utf-8 -*-
from django import forms
from surftrain.models import Train
import datetime
from django.utils import timezone


class TrainForm(forms.ModelForm):
    """
        form is responsible for working with Train model
    """
    def clean_departure(self):
        date = self.cleaned_data['departure']
        if date <= timezone.make_aware(datetime.datetime.now(), timezone.get_current_timezone()):
            raise forms.ValidationError("The date must be in the future")

        return date

    class Meta:
        model = Train
        exclude = ('arrival',)
