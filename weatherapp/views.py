# from django.shortcuts import render
# import requests
# import datetime

 
# def home(request):

#    if request.method == 'POST':
#     city = request.POST.get('city', 'mahoba')  # Correctly using .get() on request.POST
#    else:
#     city = 'mahoba'

#    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d0332b9b5e023deb670900bfc616a605'
#    PARAMS = {'units':"metric"}

#    response = requests.get(url, params=PARAMS)
#    data = response.json()


#    print(f"API response: {data}")
#    description = data['weather'][0]['description']
#    icon  = data['weather'][0]['icon']
#    temp = data['main']['temp']

#    day = datetime.date.today()


#    return render(request, 'weatherapp/index.html', {'description':description, 'icon':icon , 'temp':temp, 'day':day, 'city':city })

# from django.shortcuts import render
# import requests
# import datetime

# def home(request):
#     # Handle form submission
#    #  if request.method == 'POST':
#    #      city = request.POST.get('city', 'mahoba')  # Use .get() to avoid errors
#    #  else:
#    #      city = 'mahoba'

#    if 'city' in request.POST:
#     city = request.POST['city']
#    else:
#     city = 'indore'

#     # Make the API request
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=73b956cb7e6921151dac19cf9a6bcf3b'
#     PARAMS = {'units': 'metric'}

#     try:
#         response = requests.get(url, params=PARAMS)
#         response.raise_for_status()  # Check for HTTP errors
#         data = response.json()
        
#         description = data['weather'][0]['description']
#         icon = data['weather'][0]['icon']
#         temp = data['main']['temp']
#     except requests.RequestException as e:
#         description = 'Error fetching data'
#         icon = ''
#         temp = ''
#         print(f'Error: {e}')
    
#     day = datetime.date.today()

#     return render(request, 'weatherapp/index.html', {
#         'description': description,
#         'icon': icon,
#         'temp': temp,
#         'day': day,
#         'city': city
#     })


from django.shortcuts import render
import requests
import datetime

def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Bhagalpur'  # Default city

    # Make the API request
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=73b956cb7e6921151dac19cf9a6bcf3b'
    PARAMS = {'units': 'metric'}

    try:
        response = requests.get(url, params=PARAMS)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()

        # Debug prints
        print(f"API response: {data}")

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        description = 'Error fetching data'
        icon = ''
        temp = ''

    except KeyError as e:
        print(f"Key error: {e}")
        description = 'Data not available'
        icon = ''
        temp = ''

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city
    })
