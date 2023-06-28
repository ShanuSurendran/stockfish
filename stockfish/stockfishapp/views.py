from django.shortcuts import render
from . models import place
from . models import venue

# Create your views here.
def demo(request):
    obj=place.objects.all()
    fun=venue.objects.all()
    return render(request,"index.html",{'result':obj,'res':fun})