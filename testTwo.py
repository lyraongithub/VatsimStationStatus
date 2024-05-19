import requests
import time
from datetime import datetime, timezone

# VATSIM API endpoint for online users
url = "https://data.vatsim.net/v3/vatsim-data.json"

# Fetch the data from the VATSIM API
response = requests.get(url)
data = response.json()

# Extract controllers and flights information
controllers = data.get('controllers', [])
flights = data.get('pilots', [])

# Function to check if a specific ATC position is active
def is_atc_position_active(callsign):
    for controller in controllers:
        if controller.get('callsign') == callsign:
            return True, controller
    return False, None

# Function to count departures from a specific airport
def count_departures(airport_code):
    departures = 0
    for flight in flights:
        flight_plan = flight.get('flight_plan')
        if flight_plan is not None:
            departure_airport = flight_plan.get('departure')
            if departure_airport == airport_code:
                departures += 1
    return departures

# Function to count departures from a specific airport
def count_arrivals(airport_code):
    arrivals = 0
    for flight in flights:
        flight_plan = flight.get('flight_plan')
        if flight_plan is not None:
            departure_airport = flight_plan.get('arrival')
            if departure_airport == airport_code:
                arrivals += 1
    return arrivals

def check_status(active, zulu_time_str):
    if active:
        print(f"{zulu_time_str}\n{callsign_to_check} is active.")
        #print("Controller Info:", controller_info)
        # Count departures if station is active
        airport_code = "EGNX"  # Airport ICAO code
        num_departures = count_departures(airport_code)
        num_arrivals = count_arrivals(airport_code)
        print(f"Number of departures from {airport_code}: {num_departures}\nNumber of arrivals to {airport_code}: {num_arrivals}\n")
    else:
        print(f"{zulu_time_str}\n{callsign_to_check} is not active.\n")


while(True):
    # Check the status of station
    callsign_to_check = "EGNX_GND"
    active, controller_info = is_atc_position_active(callsign_to_check)

    current_zulu_time = datetime.now(timezone.utc)
    zulu_time_str = current_zulu_time.strftime('Current Time: %H:%Mz')

    check_status(active, zulu_time_str)
    time.sleep(60)