# from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

from .models import *

from .forms import EventForm

def index(request):
  event_list = Event.objects.order_by('date')
  context = {'event_list': event_list}
  return render(request, 'chores/index.html', context)

def roomie(request):
  roomie_list = Roomie.objects.order_by('name')
  context = {'roomie_list': roomie_list}
  return render(request, 'chores/roomie.html', context)

def chore(request):
  chore_list = Chore.objects.order_by('description')
  context = {'chore_list': chore_list}
  return render(request, 'chores/chore.html', context)

def detail(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  return render(request, 'chores/detail.html', {'event': roomie})

def results(request, chore_id):
  response = "You're looking at the results of chore %s."
  return HttpResponse(response % chore_id)

def event_new(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      event = form.save(commit=False)
      event.save()
      # return redirect('index', pk=event.pk)
  else:
    form = EventForm()
  return render(request, 'chores/event_new.html', {'form': form})