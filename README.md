# WeatherApp

WeatherApp is a responsive web application that delivers live weather information for any city or location worldwide, leveraging data from the OpenWeatherMap API. Users can search for any place and get up-to-date weather details such as temperature, humidity, wind speed etc in a clean, user-friendly interface.

## Project Purpose and Goals 

Beyond showing weather data on the frontend, WeatherApp incorporates important backend features.

- **Beginner-Friendly Django Project Structure:** It helps beginners understand how to set up a Django project with multiple pages, combining backend logic and frontend design using Bootstrap.
- **API Integration Example:** Demonstrates how to connect a Django application with an external API (OpenWeatherMap) to fetch and display live data.
- **Error & Exception Handling:** Implements input validation and uses try-except blocks to gracefully handle API failures and invalid user inputs, ensuring a smooth user experience without crashes. 
- **Form Handling & Database Interaction:** Shows how to create and process a contact form, storing user submissions in Django’s SQLite3 database.
- **Security Best Practices:** Introduces the use of environment variables to protect sensitive information like API keys and secret keys.
- **Practical Foundation:** Acts as a solid starting point for anyone looking to build more complex Django applications involving APIs, forms, and responsive UIs.

## Project Overview
- **Frameworks & Tools**: Django (Python backend), Bootstrap (HTML/CSS framework)
- **API Used**: OpenWeatherMap API (for live weather data)
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
All required Python packages are listed in `requirements.txt` at the project root directory.

## API Keys & Security
- **Django `SECRET_KEY`** and **OpenWeatherMap `API_KEY`** are hidden in the `.env` file for security.
- Users must **generate their own keys** and place them in the `.env` file to run the project.

## How to Run

### 1. Prerequisites
Ensure the following are installed on your system:

```bash
# Check for Python (better if ≥ 3.10)
python --version

# Check for Pip
pip --version

# Check for Git
git --version
```
### 2. Clone the Repository
```bash
git clone https://github.com/ShubhamChavan277/django-weatherapp.git
cd django-weatherapp
```
### 3. Create Virtual Environment (Using virtualenvwrapper-win)
```bash
# Install Virtual Environment Wrapper
pip install virtualenvwrapper-win

# Create Virtual Environment 
mkvirtualenv weatherapp_env

# Enter Into Newly Created Environment 
workon weatherapp_env
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Create `.env` File
Inside the project root/base directory, create a file named `.env`.

### 6. Generate Django `SECRET_KEY` and OpenWeatherMap `API_Key` 
####  Generate a Django `SECRET_KEY` using following command (50 characters long by default):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
#### Get an OpenWeatherMap `API_KEY`:
- Get `API_KEY` by creating an account at [OpenWeatherMap](https://openweathermap.org/) 
- OpenWeatherMap API key is usually 32 characters long.

### 7. `.env` File Format (No Spaces Around `=`)
```bash
SECRET_KEY=your_generated_secret_key
DEBUG=True
OPENWEATHER_API_KEY=your_openweather_api_key
```
`⚠` Important: Ensure there are no spaces before or after `=` to avoid `KeyError`.

### 8. Set Up Django Database and Admin Panel
```bash
python manage.py migrate
python manage.py createsuperuser
```
- `migrate` creates a fresh database (`db.sqlite3`) and sets up all the required tables using the project’s migration files, since the database file is not included in the repository.
- `createsuperuser` creates a Django admin account with username, email, and password.
- This admin account lets you log into Django’s Admin Panel at `http://127.0.0.1:8000/admin/`.
- You will be able to view and manage data submitted through features like the Contact Form here.


### 9. Run the Server
```bash
python manage.py runserver
```
✅ You’re all set! Open your browser and visit `http://127.0.0.1:8000/` to start using the application.



## WeatherApp Screenshots

### Home Page  
![Home Page](docs/screenshots/WeatherApp%20-%20Home.jpeg)

### About Page  
![About Page](docs/screenshots/WeatherApp%20-%20About.jpeg)

### Contact Page
Note: Contact details shown here are for demonstration purposes only.
![Contact Page](docs/screenshots/WeatherApp%20-%20Contact.jpeg)
