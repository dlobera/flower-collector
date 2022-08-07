from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower, Vase
from .forms import WateringForm
from django.views.generic import ListView, DetailView

# class Flower: 
#   def __init__(self, name, description):
#     self.name = name
#     self.description = description

# flowers = [
#   Flower('Dahlia', 'a genus of bushy, tuberous, herbaceous perennial plants native to Mexico and Central America.'),
#   Flower('Merigold', 'a genus of annual or perennial, mostly herbaceous plants in the family Asteraceae.'),
#   Flower('Lily', 'a genus of herbaceous flowering plants growing from bulbs, all with large prominent flowers.'),
#   Flower('Peony', 'genus Paeonia, the only genus in the family Paeoniaceae. Peonies are native to Asia, Europe and Western North America.')
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def flowers_index(request):
  flowers = Flower.objects.all()
  return render(request, 'flowers/index.html', { 'flowers': flowers })

def flowers_detail(request, flower_id):
  flower = Flower.objects.get(id=flower_id)
  watering_form = WateringForm()
  return render(request, 'flowers/detail.html', {
    'flower': flower, 'watering_form': watering_form
  })


class FlowerCreate(CreateView):
  model = Flower
  fields = '__all__'
  success_url = '/flowers/'

class FlowerUpdate(UpdateView):
  model = Flower
  fields = ['description']

class FlowerDelete(DeleteView):
  model = Flower
  success_url = '/flowers/'

def add_watering(request, flower_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.flower_id = flower_id
    new_watering.save()
  return redirect('flowers_detail', flower_id=flower_id)

class VaseCreate(CreateView):
  model = Vase
  fields = '__all__'

class VaseList(ListView):
  model = Vase

class VaseDetail(DetailView):
  model = Vase

class VaseUpdate(UpdateView):
  model = Vase
  fields = ['type', 'color']

class VaseDelete(DeleteView):
  model = Vase
  success_url = '/vases/'