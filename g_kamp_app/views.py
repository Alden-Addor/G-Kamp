from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
from django.urls import reverse
from .models import Saved

def home(request):
    return render(request, 'home.html')

def search(request):
    states = {
        "AL": 'Alabama', 
        "AK": 'Alaska',
        "AZ": 'Arizona',
        "AR": 'Arkansas',
        "CA": 'California',
        "CO": 'Colorado',
        "CT": 'Connecticut',
        "DE": 'Delaware',
        "DC": 'District Of Columbia',
        "FL": 'Florida',
        "GA": 'Georgia',
        "HI": 'Hawaii',
        "ID": 'Idaho',
        "IL": 'Illinois',
        "IN": 'Indiana',
        "IA": 'Iowa',
        "KS": 'Kansas',
        "KY": 'Kentucky',
        "LA": 'Louisiana',
        "ME": 'Maine',
        "MD": 'Maryland',
        "MA": 'Massachusetts',
        "MI": 'Michigan',
        "MN": 'Minnesota',
        "MS": 'Mississippi',
        "MO": 'Missouri',
        "MT": 'Montana',
        "NE": 'Nebraska',
        "NV": 'Nevada',
        "NH": 'New Hampshire',
        "NJ": 'New Jersey',
        "NM": 'New Mexico',
        "NY": 'New York',
        "NC": 'North Carolina',
        "ND": 'North Dakota',
        "OH": 'Ohio',
        "OK": 'Oklahoma',
        "OR": 'Oregon',
        "PA": 'Pennsylvania',
        "RI": 'Rhode Island',
        "SC": 'South Carolina',
        "SD": 'South Dakota',
        "TN": 'Tennessee',
        "TX": 'Texas',
        "UT": 'Utah',
        "VT": 'Vermont',
        "VA": 'Virginia',
        "WA": 'Washington',
        "WV": 'West Virginia',
        "WI": 'Wisconsin',
        "WY": 'Wyoming',
    }
    limits = request.GET.get('limits', 1)
    state = request.GET.get('state', None)
    page = request.GET.get('current_offset', 0)
    params = {
        'apikey': 'dfed6d80-0ffe-4284-ac92-91a0fc1b901b',
        'limit': limits,
        'offset': page,
        'state': state,
        'activity': 'camping'
    }
    data = requests.get('https://ridb.recreation.gov/api/v1/facilities', params= params).json()
    request.session['data'] = data # Using sessions to allow data to pass between different views.
    return render(request, 'search.html', {'data': data, 'current_offset': page, 'limits': limits, 'state': state, 'states': states})

def campground(request, facilityID, index): # FacilityID and index are passed in from the url to be used as data point in this API call.
    if "data" not in request.session:
        return HttpResponseRedirect(reverse('g_kamp_app:home'))
    data = request.session['data']
    page = request.GET.get('offset', 0)
    params = {
        'limit': 24,
        'offset': page
    }
    campsites = requests.get(f'https://ridb.recreation.gov/api/v1/facilities/{facilityID}/campsites?apikey=dfed6d80-0ffe-4284-ac92-91a0fc1b901b', params = params).json()
    return render(request, 'campground.html', {'campsites':campsites, 'data': data['RECDATA'][index], 'params':params, 'offset': page, 'index': index})

def getSessionData(request): # Using this to get the data from the API calls into Json information so it can be passed into JavaScript.
    data = request.session['data']
    return JsonResponse(data)

def savedCampground(request):
    if request.user.is_authenticated == True:
        campground = request.GET.get('campground')
        name= request.GET.get('name')
        Saved.objects.create(campground = campground, user = request.user, name=name)
        return JsonResponse({'message': 'Saved Campground'})
    else:
        return HttpResponseRedirect(reverse('login'))

def profile(request):
    saved_data = Saved.objects.filter(user=request.user)
    # data = request.session['data']
    return render(request, 'profile.html', {'saved_data':saved_data})

def pro_search(request, facilityID):
    data = requests.get(f'https://ridb.recreation.gov/api/v1/facilities/{facilityID}?apikey=dfed6d80-0ffe-4284-ac92-91a0fc1b901b').json()
    print(data)
    request.session['saved'] = data
    return render(request, 'pro_search.html', {'data': data})

def campsites(request, facilityID):
    saved = request.session['saved']
    page = request.GET.get('offset', 0)
    params = {
        'limit': 24,
        'offset': page
    }
    campsites = requests.get(f'https://ridb.recreation.gov/api/v1/facilities/{facilityID}/campsites?apikey=dfed6d80-0ffe-4284-ac92-91a0fc1b901b', params = params).json()
    return render(request, 'campsites.html', {'campsites': campsites, 'data': saved, 'params':params, 'offset': page,})