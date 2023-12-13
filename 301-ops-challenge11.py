#!/usr/bin/env python3

# importing request library

import requests

# Delcaring function and variables in the function for reusability
def url_request():
    # asking the user to input a url, adding https:// to the front of it
    url = input("Please type in a url (example: google.com): ")
    user_url=("https://" + url)

    # Now asking the user to select a HTTP method
    method = input("Please Select an HTTP method request\n -GET\n -POST\n -PUT\n -DELETE\n -HEAD\n -PATCH\n -OPTIONS\n")
    # Asking for confirmation
    confirmation = input(f"you have selected {user_url} with method {method}, you like to continue? y/n: ")
    # Logic statement that will cancel if they choose no
    if confirmation != "y":
        print("Operation cancelled")
        exit()

    # sending the request, getting the status code to be put through a logic statement later
    response = requests.request(method, user_url)
    status_code = response.status_code

    if status_code == 200:
        print("Website found")
    elif status_code == 201:
        print("Your data was posted!")
    elif status_code == 204:
        print("This has no content")
    elif status_code == 400:
        print("Bad request")
    elif status_code == 401:
        print("This method is not authorized")
    elif status_code == 403:
        print("This page is forbidden")
    elif status_code == 404:
        print("Page not found")
    elif status_code == 500:
        print("There is an internal server error")
    else:
        print("Invalid option")
    
    # getting the reponse header to print to screen
    print(f"Reponse header: {response.headers}")
    
#exit function

#main
url_request()

# end