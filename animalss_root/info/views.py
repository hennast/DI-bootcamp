from django.shortcuts import render
import json
# Create your views here.

with open('animalss_root\info\data.json', 'r') as f:
    data = json.load(f)

animals = data['animals']
families = data['families']

def show_family(request, id):
    family_selected = None

    for family in families:
        if family['id'] == id:
            family_selected = family
    return render(request, 'family.html', {'family': family_selected})
