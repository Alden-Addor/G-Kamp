from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.urls import reverse

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
        'offset': page, # 'page' when figuring on paging.
        'state': state,
        'activity': 'camping'
    }
    RECDATA = requests.get('https://ridb.recreation.gov/api/v1/facilities', params= params).json()
    request.session['RECDATA'] = RECDATA
    request.session['params'] = params
    return render(request, 'search.html', {'RECDATA': RECDATA, 'current_offset': page, 'limits': limits, 'state': state, 'states': states})

def campground(request, facilityID):
    if "RECDATA" not in request.session:
        return HttpResponseRedirect(reverse('g_kamp_app:home'))
    data = request.session['RECDATA']
    params = request.session['params']
    limit = params['limit']
    current_offset = params['offset']
    campsites = requests.get(f'https://ridb.recreation.gov/api/v1/facilities/{facilityID}/campsites?apikey=dfed6d80-0ffe-4284-ac92-91a0fc1b901b&limit=5&offset=0').json()
    return render(request, 'campground.html', {'campsites':campsites, 'RECDATA': data, 'params':params, 'current_offset': current_offset, 'limits': limit})
