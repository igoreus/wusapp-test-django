from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from surftrain.models import Train
from surftrain.forms import TrainForm
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

def home(request, **kwargs):
    """
        home view
    """
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = TrainForm()

    content = {
        'scheduled': Train.objects.get_scheduled().order_by('departure')[:3],
        'ongoing': Train.objects.get_ongoing().order_by('-departure'),
        'arrived': Train.objects.get_arrived().order_by('-arrival')[:3],
        'form': form
    }
    content.update(csrf(request))
    return render_to_response('surftrain/home.html', content)
