# defines database tables in py classes establishes relational links between houses, beds, and residentsfrom django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(help_text="Used for proximity trigger calculations.")
    longitude = models.FloatField(help_text="Used for proximity trigger calculations.")
    environment_type = models.CharField(
        max_length=50, 
        choices=[('quiet', 'Quiet Suburb'), ('urban', 'Urban Center'), ('rural', 'Rural/Low Density')]
    )

    def __str__(self):
        return self.name

class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    is_low_sensory = models.BooleanField(default=False, help_text="Quieter room away from main communal zones.")
    gender_designation = models.CharField(
        max_length=20, 
        choices=[('male', 'Male Only'), ('female', 'Female Only'), ('coed', 'Co-ed')]
    )

    def __str__(self):
        return f"{self.property.name} - Room {self.room_number}"

class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='beds')
    bed_label = models.CharField(max_length=20, help_text="e.g., Lower A, Top B")
    is_occupied = models.BooleanField(default=False)
    is_under_maintenance = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room} - Bed {self.bed_label}"

class ResidentProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    current_bed = models.OneToOneField(Bed, on_delete=models.SET_NULL, null=True, blank=True, related_name='resident')
    
    # Trauma-Informed Assessment Metrics
    has_claustrophobia_or_panic = models.BooleanField(default=False)
    needs_low_sensory_environment = models.BooleanField(default=False)
    
    # Spatial Trigger Coordinates (Kept secure/isolated)
    trigger_latitude = models.FloatField(blank=True, null=True, help_text="Coordinates of known trauma location.")
    trigger_longitude = models.FloatField(blank=True, null=True, help_text="Coordinates of known trauma location.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
