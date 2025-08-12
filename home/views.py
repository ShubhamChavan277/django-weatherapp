from django.shortcuts import render
import requests
from datetime import datetime, timedelta, timezone
from home.models import Contact_Form
from django.contrib import messages
from django.conf import settings

# Create your views here.
def home(request):
    # Default city: 'Mumbai' and country: 'India'
    city_input = request.GET.get('city', 'Mumbai')
    country_input = request.GET.get('country', 'IN')

    api_key = settings.OPENWEATHER_API_KEY
    
    try:    
        # If the user enters a 'country_code' along with the 'city_name', the URL inside the 'if' block will be used to request weather data for the specified city and country from the OpenWeather API.
        # If the user enters only the 'city_name', the URL inside the 'else' block will be triggered, which requests data based on the 'city_name' alone from the OpenWeather API.
        # Why is this necessary? Both approaches often work fine, but in some cases, cities with the same name exist in multiple countries. Allowing the user to enter the country code along with the city name ensures more precise results.
        # Example: The city “Rome” exists in both Italy and the USA.
        if len(country_input):
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_input},{country_input}&appid={api_key}'
        else:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}'
        data = requests.get(url).json()

        if data.get("cod") == 200:
            weather_details = {
                'code' : data['cod'],
                'city_name' : data['name'],
                'country_code' : data['sys']['country'],
                'country_code_lower' : data['sys']['country'].lower(),
                'main' : data['weather'][0]['main'],
                'description' : data['weather'][0]['description'],
                'icon' : data['weather'][0]['icon'],
                'temperature' : int(data['main']['temp'] - 273.15),
                'feels_like' : int(data['main']['feels_like'] - 273.15),
                'temp_min' : int(data['main']['temp_min'] - 273.15),
                'temp_max' : int(data['main']['temp_max'] - 273.15),
                'pressure' : data['main']['pressure'],
                'humidity' : data['main']['humidity'],
                'visibility' : int(data['visibility'] / 1000),
                'wind_speed' : data['wind']['speed'],
                'timestamp' : data['dt'],
                'timezone' : data['timezone'],
            }
            # Store valid data in the session so it persists. If the user enters an invalid city or country next time, display the data from the previous valid request.
            request.session["last_weather"] = weather_details

        # If OpenWeather API does not find any results for given input it does not return 'code:200'. Hence we raise 'ValueError' Exception.
        elif data.get("cod") != 200:
            raise ValueError("Invalid city")
        
    except (KeyError, ValueError):
        messages.warning(request, "Invalid input! Please enter a valid city/country code(optional).") 
        weather_details = request.session.get("last_weather")
    
    # Create UTC datetime object
    utc_time = datetime.fromtimestamp(weather_details.get('timestamp'), tz=timezone.utc)
    # Apply the timezone offset
    local_time = utc_time + timedelta(seconds=weather_details.get('timezone'))
    # Converts the datetime in readable format
    readable_time = local_time.strftime("%A, %d %B %Y %I:%M %p")

    context = {
        'data' : weather_details,
        'readable_time': readable_time
    }
    
    return render(request, 'index.html', context)


# About Page
def about(request):
    return render(request, 'about.html')


# Contact Page
def contact(request):
    # Retrieves the values of the contact form fields and saving it in database table
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text_message = request.POST.get('text_message')
        contact_form = Contact_Form(name=name , email=email, phone=phone, text_message=text_message, date= datetime.today())
        contact_form.save()
        messages.success(request, "You form has beed submitted successfully!")

    return render(request, 'contact.html')
    