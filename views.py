# handles incoming web requests, executes data quires, runs calculations and renders web pages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Room, Bed
from .forms import PropertyForm, RoomForm, BedForm

# this adds house info first of all
def add_house_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_obj = form.save() #this will save database
            #redirect to step 2 with new house ID
            return redirect('add_beds', property_id=property_obj.id)
        else:
            form = PropertyForm()

        return render(request, 'add_house.html', {'form' : form})

#step 2 for adding rooms, bed & truama tags for saved house

def add_bed_view(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    if requested.method == 'POST':
        room_form = RoomForm(request.POST)
        bed_form = BedForm(request.POST)
        