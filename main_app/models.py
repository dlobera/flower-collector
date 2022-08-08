from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

WATER = (
  ('1', 'Watered'),
  ('2', 'Not Watered'),
)

# Create your models here.
class Vase(models.Model):
  type = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
    return reverse('vases_detail', kwargs={'pk': self.id})


class Flower(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  vases = models.ManyToManyField(Vase)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('flowers_detail', kwargs={'flower_id': self.id})

  def watered_for_today(self):
    return self.watering_set.filter(date=date.today()).count() >= len(WATER)

class Watering(models.Model):
  date = models.DateField('Watering date')
  water = models.CharField(
    max_length=1,
    choices=WATER,
    default=WATER[0][0]
  )

  flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_water_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
