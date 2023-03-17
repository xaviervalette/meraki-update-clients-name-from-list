import requests
import json
import yaml


# Open the config.yml file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Create the URL for retrieving all network clients
url = f"https://api.meraki.com/api/v1/networks/{config['networkId']}/clients"

# Set the HTTP headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config["apiKey"]
}

# Make the API request using the requests library
response = requests.request("GET", url, headers=headers, data="")

# Print the status code of the response
print("\nRequest status code : "+str(response.status_code), "\n")

# Parse the response as JSON
responseJson = response.json()

# Print response
print(responseJson)

# Create the URL for updating all network clients
url = f"https://api.meraki.com/api/v1/networks/{config['networkId']}/clients/provision"

payload = { "clients" : [], "devicePolicy": "Normal"}

for client in config["clients"]:
    clientJson = {
    "mac": client["mac"],
    "name": client["name"]
    }

    payload["clients"].append(clientJson)

print(payload)

# Make the API request using the requests library
response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

# Print the status code of the response
print("\nRequest status code : "+str(response.status_code), "\n")

# Parse the response as JSON
responseJson = response.json()

