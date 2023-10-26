from django.db import models
from django.contrib.auth.models import User
import uuid

type_choices =(
    ('Shelter', 'shelter'),
    ('Shopping', 'shopping'),
    ('Waterfall', 'waterfall'),
    ('Lake', 'lake'),
    ('Trek', 'trek'),
    ('Temple', 'temple'),
)

class Gallery(models.Model):
    title = models.CharField(max_length=200, default="photo-site")
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.title 

class Spot(models.Model):
    spot_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    spot_type = models.CharField(max_length=120, choices=type_choices, default='N/A')
    main_image = models.ImageField(upload_to="spot_image/")
    gallery = models.ManyToManyField(Gallery)
    description = models.TextField()
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    location_url = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    
class Trip(models.Model):
    trip_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    spots = models.ManyToManyField(Spot)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    
class Profile(models.Model):
    profile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trips = models.ManyToManyField(Trip)
    
    


