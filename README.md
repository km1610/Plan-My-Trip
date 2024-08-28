# Plan My Trip: A Personalized Travel Itinerary Generator

Plan My Trip is a web application designed to simplify and enhance the travel planning experience. By gathering user inputs such as destination, travel dates, budget, and preferences, the app generates customized travel itineraries. The application also provides real-time weather forecasts for the selected destinations, ensuring a hassle-free and well-informed travel experience.

[Live Link](https://km1610.pythonanywhere.com/)

## Technology Used
### Frontend
[UIkit](https://getuikit.com/) framework for a clean, professional, and responsive user interface.

### Backend
Django framework for robust backend functionalities, including authentication, database management, and URL routing.
SQLite database for efficient, lightweight data storage.
### APIs and External Services:
- Gemini Pro API for personalized itineraries. Get the API key from [Google AI Studio](https://ai.google.dev/gemini-api)
- Visual Crossing Weather Data API for real-time weather information. Get API key by signing into [Visual Crossing](https://www.visualcrossing.com/)

## Features

- **Personalized Itinerary Generation:** Custom travel plans based on user inputs such as budget, preferences, and travel dates.
- **Weather Integration:** Real-time weather forecasts for the travel period, ensuring informed planning.
- **User Authentication:** Secure login system using Django's built-in authentication.
- **Data Storage:** Itineraries and user inputs are stored in the database for easy access and future reference.
- **Error Handling:** Robust mechanisms for managing API errors and ensuring a smooth user experience.

## Installations and Setup

### Create directory
```Bash
mkdir planmytrip
```
```Bash
cd planmytrip
```

### Cloning repo from git
```Bash
git clone https://github.com/km1610/Plan-My-Trip.git
```

### Creating Virtual Environmet
```Bash
mkvirtualenv venv
```

### Installing modules
```Bash
pip install django

pip install django_multiselectfield

pip install python-dotenv

pip install requests

pip install google-generativeai
```

### Running the application

```Bash
python manage.py runserver
```

## Future Enhancements
- **Enhanced Data Integration:** Incorporating APIs for transportation and accommodation options to create a comprehensive travel planning tool.
- **Visual Enhancements:** Including images of destinations and attractions to improve user engagement.
- **Downloadable Itineraries:** Allowing users to download their itineraries for offline access.
- **Upgraded APIs:** Utilizing premium or alternative APIs for more accurate and detailed data.
- **Personalized Recommendations:** Suggesting additional destinations and itineraries based on user preferences and travel history.
- **Multi-Currency Support:** Expanding budget inputs to include multiple currencies.

<hr>

Feel free to contribute and share your suggestions ❤️

~ Kshiti
