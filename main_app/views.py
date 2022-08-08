from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower, Vase
from .forms import WateringForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

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
class home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def flowers_index(request):
  flowers = Flower.objects.filter(user=request.user)
  return render(request, 'flowers/index.html', { 'flowers': flowers })

@login_required
def flowers_detail(request, flower_id):
  flower = Flower.objects.get(id=flower_id)
  vases_flower_doesnt_have = Vase.objects.exclude(id__in = flower.vases.all().values_list('id'))
  watering_form = WateringForm()
  return render(request, 'flowers/detail.html', {
    'flower': flower, 'watering_form': watering_form, 'vases': vases_flower_doesnt_have
  })


class FlowerCreate(LoginRequiredMixin, CreateView):
  model = Flower
  fields = '__all__'
  success_url = '/flowers/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class FlowerUpdate(LoginRequiredMixin, UpdateView):
  model = Flower
  fields = ['description']

class FlowerDelete(LoginRequiredMixin, DeleteView):
  model = Flower
  success_url = '/flowers/'

@login_required
def add_watering(request, flower_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.flower_id = flower_id
    new_watering.save()
  return redirect('flowers_detail', flower_id=flower_id)

class VaseCreate(LoginRequiredMixin, CreateView):
  model = Vase
  fields = '__all__'

class VaseList(LoginRequiredMixin, ListView):
  model = Vase

class VaseDetail(LoginRequiredMixin, DetailView):
  model = Vase

class VaseUpdate(LoginRequiredMixin, UpdateView):
  model = Vase
  fields = ['type', 'color']

class VaseDelete(LoginRequiredMixin, DeleteView):
  model = Vase
  success_url = '/vases/'

@login_required
def assoc_vase(request, flower_id, vase_id):
  Flower.objects.get(id=flower_id).vases.add(vase_id)
  return redirect('flowers_detail', flower_id=flower_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('flowers_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)