# FILE: google_books.py
# PURPOSE: This file handles all communication with the Google Books API.

import requests

# Fetches book details using its ISBN

def get_book_details(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Parse the JSON data to find the relevant book information
        if 'items' in data and data['items']:
            book_info = data['items'][0]['volumeInfo']
            title = book_info.get('title', 'No Title Found')
            authors = book_info.get('authors', ['Unknown Author'])
            author = authors[0]
            
            # Get the image link
            image_links = book_info.get('imageLinks', {})
            thumbnail = image_links.get('thumbnail', None)
            
            return {'title': title, 'author': author, 'cover_url': thumbnail}
            
    except requests.exceptions.RequestException:
        # Handle cases where the internet connection fails or the API is down
        print(f"Error connecting to Google Books API: {e}")
        return None
    return None

