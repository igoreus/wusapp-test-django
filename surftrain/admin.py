# -*- coding: utf-8 -*-
from django.contrib import admin
from surftrain.models import Train

class TrainAdmin(admin.ModelAdmin):
    list_display = ['description', 'user', 'status', 'departure', 'arrival']
admin.site.register(Train, TrainAdmin)

