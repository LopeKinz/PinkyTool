import requests
import base64
import json
import time

def discord_token_analyzer():
    token = input("Enter the Discord token to analyze: ")
    
    # Decode the token payload
    try:
        token_parts = token.split('.')
        encoded_payload = token_parts[1]
        decoded_payload = base64.b64decode(encoded_payload + "==").decode("utf-8")
        payload_data = json.loads(decoded_payload)
    except (IndexError, TypeError, json.JSONDecodeError):
        print("Invalid token format or payload could not be decoded.")
        return
    
    print("Token Information:")
    print("Bearer Type:", token_parts[0])
    print("Token Signature:", token_parts[2])
    print()
    print("Payload Data:")
    print("User ID:", payload_data.get("id"))
    print("Username:", payload_data.get("username"))
    print("Discriminator:", payload_data.get("discriminator"))
    print("Email:", payload_data.get("email"))
    print("Avatar Hash:", payload_data.get("avatar"))
    print("Token Issued At (Unix Timestamp):", payload_data.get("iat"))
    print("Token Expires At (Unix Timestamp):", payload_data.get("exp"))
    print("Is Token Valid (Not Expired):", payload_data.get("exp") > time.time())

def main_menu():
    while True:
        print("=== Main Menu ===")
        print("1. URL Shortener")
        print("2. IP Lookup")
        print("3. Discord Token Analyzer")
        print("0. Exit")
        choice = input("Enter your choice (0-3): ")
        print()

        if choice == "1":
            url_shortener()
        elif choice == "2":
            ip_lookup()
        elif choice == "3":
            discord_token_analyzer()
        elif choice == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        print()

def url_shortener():
    url = input("Enter the URL to shorten: ")
    response = requests.post("https://tinyurl.com/api-create.php?url=" + url)
    if response.status_code == 200:
        shortened_url = response.text
        print("Shortened URL:", shortened_url)
    else:
        print("Error occurred while shortening the URL.")

def ip_lookup():
    ip = input("Enter the IP address to lookup: ")
    response = requests.get("http://ip-api.com/json/" + ip)
    if response.status_code == 200:
        data = response.json()
        print("IP Address:", data["query"])
        print("Country:", data["country"])
        print("City:", data["city"])
        print("ISP:", data["isp"])
    else:
        print("Error occurred while performing IP lookup.")

# Start the program
main_menu()
