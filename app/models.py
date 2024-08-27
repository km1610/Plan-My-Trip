from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from multiselectfield import MultiSelectField
import uuid
# Create your models here.
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email')

class Itinerary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    input_id = models.UUIDField()
    username = models.CharField(max_length=50)
    itinerary = models.TextField()

TRAVEL_COMPANIONS = (
    ('family', 'Family'),
    ('friends', 'Friends'),
    ('partner', 'Partner'),
    ('solo', 'Solo'),
    ('doesnt_matter', 'Doesn’t Matter'),
)

PREFERENCES = (
    ('adventure', 'Adventure: Activities like hiking, rafting, zip-lining, etc.'),
    ('cultural', 'Cultural: Museums, historical sites, cultural tours, local experiences.'),
    ('relaxation', 'Relaxation: Beach resorts, spas, leisurely activities.'),
    ('nature_wildlife', 'Nature & Wildlife: National parks, safaris, nature trails, bird watching.'),
    ('amusement_parks', 'Amusement Parks: Theme parks, water parks, fun fairs.'),
    ('religious_spiritual', 'Religious/Spiritual: Pilgrimages, visits to temples, churches, mosques, meditation retreats.'),
    ('trekking', 'Trekking: Mountain treks, hiking trails, nature walks.'),
    ('food_culinary', 'Food & Culinary: Food tours, cooking classes, street food experiences, wine tasting.'),
    ('shopping', 'Shopping: Markets, shopping malls, local crafts.'),
    ('nightlife', 'Nightlife: Bars, clubs, live music, entertainment.'),
    ('festivals_events', 'Festivals & Events: Local festivals, music concerts, cultural events.'),
    ('art_architecture', 'Art & Architecture: Art galleries, architectural landmarks, design tours.'),
    ('photography', 'Photography: Scenic spots, photogenic locations, guided photography tours.'),
    ('wellness_spa', 'Wellness & Spa: Yoga retreats, wellness centers, spa treatments.'),
    ('offbeat_experiences', 'Offbeat Experiences: Unique, unconventional, and less crowded places.'),
    ('family_friendly', 'Family-Friendly: Activities suitable for all ages, family tours.'),
    ('doesnt_matter', 'Does not matter: Open to any kind of experience.')
)

class Itinerary_Input(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=50)
    from_address = models.CharField(max_length=100)
    to_address = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    budget = models.DecimalField(max_digits=18,decimal_places=2)
    adults = models.IntegerField()
    children = models.IntegerField()
    travel_companion = models.CharField(choices = TRAVEL_COMPANIONS,max_length=50)
    preferences = MultiSelectField(choices = PREFERENCES,default='doesnt_matter')
    special_requests = models.TextField()


class ItineraryForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    from_address = forms.CharField(max_length=100)
    to_address = forms.CharField(max_length=100)
    from_date = forms.DateField()
    to_date = forms.DateField()
    budget = forms.DecimalField()
    adults = forms.IntegerField()
    children = forms.IntegerField()
    travel_companion = forms.ChoiceField(choices = TRAVEL_COMPANIONS)
    preferences = forms.MultipleChoiceField(choices = PREFERENCES,widget=forms.CheckboxSelectMultiple)
    special_requests = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Itinerary_Input
        fields = ['username', 'from_address', 'to_address', 'from_date', 'to_date', 'budget', 'adults', 'children', 'travel_companion', 'preferences', 'special_requests']



