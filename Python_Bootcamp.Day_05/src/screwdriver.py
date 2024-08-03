import os
from bs4 import BeautifulSoup
import requests
import sys

SERVER_URL = 'http://127.0.0.1:8888'


def upload_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        files = {'file': (filename, f)}
        response = requests.post(SERVER_URL, files=files)
        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print("File upload failed")


def list_files():
    response = requests.get(SERVER_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        files_list = soup.find_all('a')
        print("Files on server:")
        for file in files_list:
            print(file.get_text())
    else:
        print(f"Failed to retrieve file list. Status code: {response.status_code}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python screwdriver.py [upload/list] [file_path]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "upload":
        if len(sys.argv) != 3:
            print("Usage: python screwdriver.py upload /path/to/file.mp3")
            sys.exit(1)
        file = sys.argv[2]
        upload_file(file)
    elif action == "list":
        list_files()
    else:
        print("Unknown action. Use 'upload' or 'list'")
        sys.exit(1)
