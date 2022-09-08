from django.shortcuts import render

# Create your views here.
def homepage(request):
   return render(request, 'choosetype.html')

def cardio(request):
   return render(request, 'cardio.html')

def strength(request):
   return render(request, 'strength.html')

def speed(request):
   return render(request, 'speed.html')

def endurance(request):
   return render(request, 'endurance.html')
