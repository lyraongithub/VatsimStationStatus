import requests  # Import the requests library to make HTTP requests

# VATSIM API endpoint for online users
url = "https://data.vatsim.net/v3/vatsim-data.json"

# Fetch the data from the VATSIM API
response = requests.get(url)  # Make a GET request to the API
data = response.json()  # Parse the response as JSON

# Extract controllers information from the parsed data
controllers = data.get('controllers', [])  # Get the list of online controllers

# Function to check if a specific ATC position is active
def is_atc_position_active(callsign):
    for controller in controllers:  # Iterate through the list of controllers
        if controller.get('callsign') == callsign:  # Check if the callsign matches
            return True, controller  # Return True and the controller's info if match is found
    return False, None  # Return False if no match is found

# Example usage
callsign_to_check = "EGPH_GND"  # Replace with the desired ATC position callsign
active, controller_info = is_atc_position_active(callsign_to_check)  # Call the function to check the position

if active:  # If the position is active
    print(f"{callsign_to_check} is active.")  # Print that the position is active
    #print("Controller Info:", controller_info)  # Print the controller's information
else:  # If the position is not active
    print(f"{callsign_to_check} is not active.")  # Print that the position is not active
