from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .models import RegistrationForm, ItineraryForm, Itinerary_Input, Itinerary
from .functions import GenerateItinerary, FetchWeatherData, GetCity
import json
# Create your views here.
@guest
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password1':'','password2':'','first_name':'','last_name':'','email':''}
        form = RegistrationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@auth
def dashboard_view(request):
    itinerary_inputs = Itinerary_Input.objects.all().values()
    return render(request, 'dashboard.html',{'itinerary_inputs':itinerary_inputs})

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'index.html')

@auth
def itinerary_view(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)

        if form.is_valid():
            data = form.save()
            itinerary = GenerateItinerary(data)
            weather_data = FetchWeatherData(GetCity(data),data)
            new_itinerary = Itinerary.objects.create(input_id = data.id, username = data.username, itinerary=itinerary)

            try:
                render(request, 'itinerary/result.html',{'data':data,'itinerary':None,'weather_data':None})
            except:
                Itinerary_Input.objects.get(id = data.id).delete()
                Itinerary.objects.get(id = new_itinerary.id).delete()
                return render(request, 'error.html')

            try:
                render(request, 'itinerary/result.html',{'data':data,'itinerary':itinerary,'weather_data':None})
            except:
                Itinerary_Input.objects.get(id = data.id).delete()
                Itinerary.objects.get(id = new_itinerary.id).delete()
                return render(request, 'itinerary/result.html',{'data':data,'itinerary':None,'weather_data':None})

            try:
                render(request, 'itinerary/result.html',{'data':data,'itinerary':itinerary,'weather_data':weather_data})
            except:
                return render(request, 'itinerary/result.html',{'data':data,'itinerary':itinerary,'weather_data':None})
                

            return render(request, 'itinerary/result.html',{'data':data,'itinerary':itinerary,'weather_data':weather_data})
                
    else:
        initial_data = {'username':'', 'from_address':'', 'to_address':'', 'from_date':'', 'to_date':'', 'budget':'', 'adults':'', 'children':'', 'travel_companion':'', 'preferences':'', 'special_requests':''}
        form = ItineraryForm(initial=initial_data)

    return render(request, 'itinerary/form.html',{'form':form})

@auth
def old_itinerary_view(request,id):
    iternary_input = Itinerary_Input.objects.get(id = id)
    itinerary = Itinerary.objects.get(input_id = id)
    weather_data = FetchWeatherData(GetCity(iternary_input),iternary_input)
    try:
        render(request, 'itinerary/result.html',{'data':iternary_input,'itinerary':itinerary.itinerary,'weather_data':None})
    except:
        return render(request, 'error.html')

    try:
        render(request, 'itinerary/result.html',{'data':iternary_input,'itinerary':itinerary.itinerary,'weather_data':weather_data})
    except:
        return render(request, 'itinerary/result.html',{'data':iternary_input,'itinerary':itinerary.itinerary,'weather_data':None})

    return render(request, 'itinerary/result.html',{'data':iternary_input,'itinerary':itinerary.itinerary,'weather_data':weather_data})

def clear_itinerary_view(request):
    Itinerary_Input.objects.filter(username = request.user.username).delete()
    Itinerary.objects.filter(username = request.user.username).delete()
    itinerary_inputs = Itinerary_Input.objects.all().values()
    return render(request, 'dashboard.html',{'itinerary_inputs':itinerary_inputs})

def delete_itinerary_view(request,id):
    Itinerary_Input.objects.get(id = id).delete()
    Itinerary.objects.get(input_id = id).delete()
    itinerary_inputs = Itinerary_Input.objects.all().values()
    return render(request, 'dashboard.html',{'itinerary_inputs':itinerary_inputs})

def contact_view(request):
    return render(request,'contact.html')
        