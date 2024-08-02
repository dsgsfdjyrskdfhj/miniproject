import requests
import random
import json
import string

# Base URL
base_url = "https://postman-library-api.glitch.me"

# Authentication
username = "sutharsini"
password = "sutharsini@"

# Helper function to generate random book data
def generate_random_book_data():
    return {
        "title": ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
        "author": ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
        "genre": random.choice(["fiction", "non-fiction", "drama", "mystery"]),
        "yearPublished": random.randint(1900, 2023)
    }

# GET Requests
def get_books():
    url = base_url + "/books"
    headers = {
        "Authorization": "Basic " + requests.auth._basic_auth_str(username, password)
    }
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

def get_book(book_id):
    url = base_url + f"/books/{book_id}"
    headers = {
        "Authorization": "Basic " + requests.auth._basic_auth_str(username, password)
    }
    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

# POST Requests
def add_book():

    """url = base_url + "/books"
    headers = {
            "Authorization": "Basic " + requests.auth._basic_auth_str(username, password),
            "Content-Type": "application/json"
    }
    book_data = generate_random_book_data()
    response = requests.post(url, headers=headers, data=json.dumps(book_data))
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print("Book Added:", book_data)"""


    url = base_url + "/books"
    headers = {
            "Authorization": "Basic " + requests.auth._basic_auth_str(username, password),
            "Content-Type": "application/json"
    }
    book_data = {
            "title": "Adventures in Wonderland",
            "author": "Carroll",
            "genre": "fiction",
            "yearPublished": 2014,
            "checkedOut":False

    }
    response = requests.post(url, headers=headers, data=json.dumps(book_data))
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print("Book Added:\n", book_data)
    #for key, value in book_data.items():
            #print(f"{key.capitalize()}: {value}")
    print(response.json().get('id') ) # Return the ID of the added book


# PATCH Requests
def patch_update_book(book_id):
    url = base_url + f"/books/{book_id}"
    headers = {
        "Authorization": "Basic " + requests.auth._basic_auth_str(username, password),
        "Content-Type": "application/json"
    }
    patch_data = {
        "title": "Patched Title"
    }
    response = requests.patch(url, headers=headers, data=json.dumps(patch_data))
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    """url = base_url + "/books/" + book_data["book_id"]
    headers = {
        "Authorization": "Basic " + requests.auth._basic_auth_str(username, password),
        "Content-Type": "application/json"
    }
    updated_book_data = {
        "title": "Alice's Adventures in Wonderland",
        "author": "Lewis Carroll",
        "genre": "fiction",
        "yearPublished": 1965,
        "checkedOut": False
    }
    response = requests.put(url, headers=headers, data=json.dumps(updated_book_data))
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    print("Book Updated:", updated_book_data)"""

# DELETE Requests
"""def delete_book(book_id):
    url = base_url + f"/books/{book_id}"
    headers = {
        "Authorization": "Basic " + requests.auth._basic_auth_str(username, password)
    }
    response = requests.delete(url, headers=headers)
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())"""

# Testing the functions
print("GET all books:")
get_books()


#print("\nPOST add book:")
#add_book()


book_id = "z__zWO4uYG46i6W"

print("\nGET single book:")
get_book(book_id)

print("\nPOST add book:")
add_book()

print("\nPATCH update book:")
patch_update_book(book_id)


#print("\nDELETE book:")
#delete_book(book_id)



