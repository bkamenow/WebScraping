import json
import os
import re

import requests
from bs4 import BeautifulSoup


def sort_info(info):
    return sorted(info, key=lambda x: float(x[1].replace(' лв.', '')))


def get_info(url, pattern, replace_list=None):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the list of item and iterate through each article
    list_results = soup.find(id='list-results')
    articles = list_results.find_all('article')

    info = []

    # Extract desk name and price for each article
    for ar in articles:
        title = ar.find(class_='ttl').text
        match = re.search(pattern, title)
        if match:
            name = match.group(1)
            price = ar.find(class_='price').text.strip()

            if replace_list:
                for replace_item in replace_list:
                    name = name.replace(replace_item, '')

            info.append((name, price))

    sort_list = sort_info(info)

    return sort_list


def load_existing_info(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return []
    return []


def update_info(existing_info, new_info, file_path):
    updated_info = existing_info.copy()
    for desk_name, price in new_info:
        # Check if the desk name is not already present in the existing information
        if not any(desk_name in desk for desk in existing_info):
            updated_info.append({desk_name: price})

    # Write the updated desk information to the JSON file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(updated_info, file, indent=4, ensure_ascii=False)

    return updated_info


def print_info(info):
    print('Name: Price')
    for name, price in info:
        print(f"{name}: {price}")
