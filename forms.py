from django import forms
from .models import Property, Room, Bed
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['organization', 'name', 'address', 'city', 'county', 'is_marr_certified', 'narr_level', 'environment_type', 'latitude', 'longitude']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'floor', 'gener_designation', 'is_low_sensory', 'has_private_bathroom']

class BedForm(forms.ModelForm):
    class Meta:
        fields = ['bed_label', 'status', 'bunk_possition', 'is_corner_anchor', 'has_direct_window', 'is_ada_accessible']