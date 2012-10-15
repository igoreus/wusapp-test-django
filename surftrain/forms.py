# -*- coding: utf-8 -*-
from django import forms
from surftrain.models import Train


class TrainForm(forms.ModelForm):
    """
        form is responsible for working with Train model
    """
    class Meta:
        model = Train
