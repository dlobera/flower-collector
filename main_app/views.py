from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Flower

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
  return render(request, 'flowers/detail.html', { 'flower': flower })

class FlowerCreate(CreateView):
  model = Flower
  fields = '__all__'