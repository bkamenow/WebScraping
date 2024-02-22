import os
import re
import json
import requests
from bs4 import BeautifulSoup


def get_gaming_desks_info(url):
    pattern = r'бюро\s+(.*?)(?=,|\d{3}/\d{2}/\d{2}\sсм)'

    # Send a GET request to the URL and parse the HTML content
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the list of desks and iterate through each desk article
    desks_list = soup.find(id='list-results')
    articles = desks_list.find_all('article')

    gaming_desk_info = []

    # Extract desk name and price for each article
    for ar in articles:
        title = ar.find(class_='ttl').text
        match = re.search(pattern, title)
        if match:
            # Clean the desk name and remove unnecessary phrases
            desk_name = (match.group(1).strip()
                         .replace(' с поставка за монитор', '')
                         .replace(' с регулируема височина', '')
                         .replace(' с електрическо управление', ''))

            price = ar.find(class_='price').text.strip()
            gaming_desk_info.append((desk_name, price))

    return sorted(gaming_desk_info, key=lambda x: float(x[1].replace(' лв.', '')))


def load_existing_desks_info(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return []
    return []


def update_desks_info(existing_desk_info, new_desk_info, file_path):
    updated_desk_info = existing_desk_info.copy()
    for desk_name, price in new_desk_info:
        # Check if the desk name is not already present in the existing information
        if not any(desk_name in desk for desk in existing_desk_info):
            updated_desk_info.append({desk_name: price})

    # Write the updated desk information to the JSON file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(updated_desk_info, file, indent=4, ensure_ascii=False)

    return updated_desk_info


def main():
    url_page1 = 'https://plasico.bg/game-zone/geymyrski-byura'
    url_page2 = 'https://plasico.bg/game-zone/geymyrski-byura/p2'
    file_path = 'gaming_desks.json'

    try:
        # Get gaming desk information from both pages
        new_desk_info_page1 = get_gaming_desks_info(url_page1)
        new_desk_info_page2 = get_gaming_desks_info(url_page2)

        # Combine desk information from both pages
        new_desk_info = new_desk_info_page1 + new_desk_info_page2

        # Load existing desk information from the JSON file
        existing_desk_info = load_existing_desks_info(file_path)

        # Update existing desk information with new entries
        updated_desk_info = update_desks_info(existing_desk_info, new_desk_info, file_path)

        # Check if new information has been added
        if len(updated_desk_info) != len(existing_desk_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        print('Name: Price')
        for desk_name, price in new_desk_info:
            print(f"{desk_name}: {price}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
