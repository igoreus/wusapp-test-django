from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def home(request, **kwargs):
    """
        home view
    """
    content = []
    return render_to_response('surftrain/home.html', content)
