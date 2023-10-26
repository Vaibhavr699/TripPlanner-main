from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator
from .models import Spot, Profile, Trip

def is_valid_param(param):
    return param != "" and param != None

def index(request): 

    spots = Spot.objects.all()

    context = {
        'temples': spots.filter(spot_type__icontains="temple"),
        'shopping': spots.filter(spot_type__icontains="shopping"),
        'waterfalls': spots.filter(spot_type__icontains="waterfall"),
        'lakes': spots.filter(spot_type__icontains="lake"),
        'shelters': spots.filter(spot_type__icontains="shelter"),
    }


    return render(request, 'index.html', context)

def spot_detail(request, pk):
    spot = Spot.objects.filter(slug=pk).first()
    trips = None
    if request.user:
        user = User.objects.filter(username=request.user.username).first()
        profile = Profile.objects.filter(user=user).first()
        if profile:
            if profile.trips.exists():
                trips = profile.trips

    context = {
        'spot': spot,
        'trips': trips,
    }

    return render(request, 'spot-details.html', context)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists() == False:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)

            user = User.objects.filter(username=username).first()
            profile = Profile.objects.create(user=user)
            profile.save()

            return redirect('/')
    else:
         return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')

def search_spot(request):
    spots = Spot.objects.all()
    search_include = request.GET.get('search_include')

    trips = None
    if request.user:
        user = User.objects.filter(username=request.user.username).first()
        profile = Profile.objects.filter(user=user).first()
        if profile:
            if profile.trips.exists():
                trips = profile.trips
    
    if is_valid_param(search_include):
        spots = spots.filter(city__icontains=search_include)

    paginator = Paginator(spots, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'search_include': search_include,
        'spots': page_obj,
        'trips': trips,
    }

    return render(request, 'spot-listing.html', context)

def create_trip(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.user.username).first()
        profile = Profile.objects.filter(user=user).first()

        trip_name = request.POST['trip_name']
        trip_note = request.POST['trip_note']
        spot_id = request.POST['spot_id']


        spot = Spot.objects.filter(spot_id=spot_id).first()
        trip = Trip.objects.create(title=trip_name, note=trip_note)
        trip.spots.add(spot)
        trip.save()
        trip_id = trip.trip_id

        trip = Trip.objects.filter(trip_id=trip_id).first()
        profile.trips.add(trip)

        return redirect(f'/spot/{spot.slug}')
    else:
        trip_name = request.GET.get('name')    
        spot_id = request.GET.get('spot_id')  
        
        spot = Spot.objects.filter(spot_id=spot_id).first()
        trip_obj = Trip.objects.create(title=trip_name)
        trip_obj.spots.add(spot)
        trip_obj.save()
        trip_id = trip_obj.trip_id
        

        user = User.objects.filter(username=request.user.username).first()
        profile = Profile.objects.filter(user=user).first()
        trip = Trip.objects.filter(trip_id=trip_id).first()
        profile.trips.add(trip)

        return redirect(f"/search-spot?search_include={spot.city}")
    
def add_spot(request):
    spot_id = request.GET.get('spotId')
    trip_id = request.GET.get('tripId')

    spot = Spot.objects.filter(spot_id=spot_id).first()
    trip = Trip.objects.filter(trip_id=trip_id).first()

    trip.spots.add(spot)

    return redirect(f'/search-spot?search_include={spot.city}')

def user_trip_list(request):
    user = User.objects.filter(username=request.user.username).first()
    profile = Profile.objects.filter(user=user).first()
    user_trips = profile.trips.all()

    context = {
        'user': user,
        'trips': user_trips
    }
    
    return render(request, 'trip-list.html', context)

def user_trip_detail(request, pk):
    trip = Trip.objects.filter(trip_id=pk).first()
    spots = trip.spots.all()

    context = {
        'trip': trip,
        'spots': spots,
    }
    return render(request, 'trip-detail.html', context)

def user_trip_delete(request, pk):
    Trip.objects.filter(trip_id=pk).delete()
    return redirect('/my-trip-list/')
