import re
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
import google.generativeai as genai
import pyttsx3
import requests
import os
from dotenv import load_dotenv

load_dotenv()
def GenerateItinerary(data):
    genai.configure(api_key=os.environ.get("GEN_AI_API"))

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content([f"Generate an itinerary for {data.to_address} from {data.from_date} to {data.to_date} considering that there are {data.adults} adults and {data.children} children for the trip and budget for the trip is {data.budget} INR and travel companion will be {data.travel_companion} and specific preferences for the trip should be {data.preferences} and for special requests we have {data.special_requests}. Traveller/s will be travelling from {data.from_address}"],safety_settings=[{
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
    },{
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_NONE",
    },{
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_NONE",
    },{
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_NONE",
    }])

    return response.text

def GetCity(data):
    genai.configure(api_key=os.environ.get("GEN_AI_API"))

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content([f"If {data.to_address} is a city then just give {data.to_address} otherwise give its capital city. Just the name of the city and nothing else!Don't form any sentences!"])

    return response.text

def FetchWeatherData(to_address, data):
  to_date = data.to_date.strftime('%Y-%m-%d')
  from_date = data.from_date.strftime('%Y-%m-%d')
  api_key = os.environ.get("WEATHER_API_1")
  response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{to_address}/{from_date}/{to_date}?key={api_key}")
  print(response)
  print(os.environ.get("WEATHER_API_2"))
  return response.json