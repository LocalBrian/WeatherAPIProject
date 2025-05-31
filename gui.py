# Will handle all of the GUI related code
# Importing the necessary libraries
import tkinter as tk
import requests

# Create a class instance for the GUI
class WeatherAppGUI:
    
    def __init__(self, master, a_p_key):
        self.master = master
        self.master.geometry("600x400")
        self.master.option_add("*Font", "Helvetica 20")
        self.master.title("Weather App")
        self.a_p_key = a_p_key # Slight obfuscation for if people are doing key word search somehow over my repositories
        
        # Create a label for the zip code input
        self.zip_code = tk.Label(master, text="Enter Zip Code (Format as: #####):")
        self.zip_code.pack()
        
        # Create an entry widget for the zip code input
        self.zip_entry = tk.Entry(master)
        self.zip_entry.pack()
    
        # Create a button to fetch weather data
        self.fetch_button = tk.Button(master, text="Get Weather", command=self.return_weather)
        self.fetch_button.pack()
        
        # Create a label to display the weather data
        self.weather_label = tk.Label(master, text="Waiting for zip code input...")
        self.weather_label.pack()
    
    def return_weather(self):
        
        # Verify that a proper zip code has been entered
        zip_code = self.zip_entry.get()
        if len(zip_code) == 5 and zip_code.isdigit():
            pass
        else:
            self.weather_label.config(text="Please enter a valid 5-digit zip code.")
            return
            
        # Make API call to fetch latitude and longitude
        return_data = self.api_lat_lon(zip_code)
        
        # Verify that proper latitude and longitude have been returned
        if return_data is None:
            self.weather_label.config(text="Error fetching latitude and longitude from zip code. Please try again later.")
            return
        
        # Make API call to fetch weather data
        return_weather = self.api_weather(return_data['lat'], return_data['lon'])
        
        # Verify that proper weather data has been returned
        if return_weather is None:
            self.weather_label.config(text="Error fetching weather data. Please try again later.")
            return
        
        # Display the weather data
        self.display_weather(return_weather)
        
        pass
        
    def api_lat_lon(self, zip_code):
        
        # Convert the zip code to a URL for the latitude and longitude portions of API
        geo_url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={self.a_p_key}"
        
        try:
            response = requests.get(geo_url)
            if (response.status_code == 200):
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data location: {e}")
            self.weather_label.config(text="Error fetching location data. Please try again.")
            return
        
        # Return nothing if anything but successful
        return
    
    def api_weather(self, lat, lon):
        
        # Format lat and long to be 2 decimal places
        lat = f"{lat:.2f}"
        lon = f"{lon:.2f}"
        
        # Convert the latitude and longitude to a URL for the weather data portion of API
        weather_url = f"https://pro.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={self.a_p_key}"
        
        try:
            response = requests.get(weather_url)
            if (response.status_code == 200):
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data weather: {e}")
            self.weather_label.config(text="Error fetching weather data. Please try again.")
            return
        
        # Return nothing if anything but successful
        return
        
    def display_weather(self, weather_data):
        
        # Retrieve the data from the weather data
        city = weather_data.get('name', 'Unknown City')
        temp = weather_data['main'].get('temp', 'Unknown Temperature')
        feels_like = weather_data['main'].get('feels_like', 'Unknown Feels Like')
        humidity = weather_data['main'].get('humidity', 'Unknown Humidity')
        description = weather_data['weather'][0].get('description', 'Unknown Description')
        wind_speed = weather_data['wind'].get('speed', 'Unknown Wind Speed')
        
        # Format the weather data into a string
        weather_info = (f"City: {city}\n"
                        f"Temperature: {temp}°F\n"
                        f"Feels Like: {feels_like}°F\n"
                        f"Description: {description}\n"
                        f"Wind Speed: {wind_speed} mph\n"
                        f"Humidity: {humidity}%")
        
        # Update the weather label with the formatted weather data
        self.weather_label.config(text=weather_info)
        
        