import openpyxl
import requests

# Replace with your NowPayments API key
NOWPAYMENTS_API_KEY = ""

# The endpoint for checking payment status
NOWPAYMENTS_API_STATUS_ENDPOINT = "https://api.nowpayments.io/v1/payment"

# Replace with the specific payment ID you want to check
payment_id = ""

# Construct the API URL for checking payment status
url = f"https://api.nowpayments.io/v1/payment/{payment_id}"

# Set the headers with the API key
headers = {
    "x-api-key": NOWPAYMENTS_API_KEY
}

# Make a GET request to the NowPayments API
response = requests.get(url, headers=headers)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Here you can handle the data as you prefer
    print(data)
else:
    # Print an error message if the status code is not 200
    print(f"Error while checking payment status: {response.text}")
