import subprocess
import sys

# List of required packages
required_packages = ['google_image_fetcher']  

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install(package)



# required_packages -> pip install google_image_fetcher

from google_image_fetcher.google_image_fetcher import GoogleImageFetcher

# Create a GoogleImageFetcher instance

fetcher = GoogleImageFetcher()


# Define the search query

# query = input("enter the word you want to search ")
query = "car"

# Fetch and save images

fetcher.fetch_images(query, save_folder="output")