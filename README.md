# WeatherApp

WeatherApp is a responsive web application that delivers live weather information for any city or location worldwide, leveraging data from the OpenWeather API. Users can search for any place and get up-to-date weather details such as temperature, humidity, wind speed etc in a clean, user-friendly interface.

## Project Purpose and Goals 

Beyond showing weather data on the frontend, WeatherApp incorporates important backend features.

- **Beginner-Friendly Django Project Structure:** It helps beginners understand how to set up a Django project with multiple pages, combining backend logic and frontend design using Bootstrap.
- **API Integration Example:** Demonstrates how to connect a Django application with an external API (OpenWeather) to fetch and display live data.
- **Error & Exception Handling:** Implements input validation and uses try-except blocks to gracefully handle API failures and invalid user inputs, ensuring a smooth user experience without crashes. 
- **Form Handling & Database Interaction:** Shows how to create and process a contact form, storing user submissions in Django’s SQLite3 database.
- **Security Best Practices:** Introduces the use of environment variables to protect sensitive information like API keys and secret keys.
- **Practical Foundation:** Acts as a solid starting point for anyone looking to build more complex Django applications involving APIs, forms, and responsive UIs.

## Project Overview
- **Frameworks & Tools**: Django (Python backend), Bootstrap (HTML/CSS framework)
- **API Used**: OpenWeather API (for live weather data)
- **Database**: SQLite3 (Django's default local database) for storing Contact Form submissions
- **Current Pages**:
  1. **Home** – Displays live weather for a given city on a Bootstrap card for a clean, modern feel.
  2. **About** – Information about the application.
  3. **Contact** – Allows users to submit queries/suggestions via a contact form (data saved locally).

## Input Fields
- **City Name** – **Required**. Without it, the search will not be triggered.
- **Country Code** – Optional 2-letter country code (ISO 3166-1 alpha-2) for precise results when a city name exists in multiple countries.  
  *Example*: `Rome, IT` vs. `Rome, US`.

## Error & Exception Handling
- Uses **try-except blocks** to catch API request failures (e.g., invalid city name, network errors) and displays user-friendly error messages using Django messages framework and Bootstrap alerts.
- Client-side input validation (HTML form attributes like `required` and `maxlength`) prevents incorrect form submissions before they reach the server.

## Requirements
All required Python packages are listed in `requirements.txt` at the project root.

## API & Security
- **Django SECRET_KEY** and **OpenWeather API Key** are hidden in the `.env` file for security.
- Users must **generate their own keys** to run the project.

## WeatherApp Screenshots

### Home Page  
![Home Page](docs/screenshots/WeatherApp%20-%20Home.jpeg)

### About Page  
![About Page](docs/screenshots/WeatherApp%20-%20About.jpeg)

### Contact Page
Note: Contact details shown here are for demonstration purposes only.
![Contact Page](docs/screenshots/WeatherApp%20-%20Contact.jpeg)
