""" This script encodes a sequences of characters. 
The aim is to encode special characters in passwords"""

import urllib.parse

# Get user input for the password
password = input("Enter the password: ")

# Encode the password using urllib.parse.quote_plus()
encoded_password = urllib.parse.quote_plus(password)

# Print the encoded password
print("Encoded password:", encoded_password)
