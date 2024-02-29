import json
import os
import re

import requests
from bs4 import BeautifulSoup


def sort_info(info):
    return sorted(info, key=lambda x: float(x[1].replace(' лв.', '')))


def print_info(info):
    print('Name: Price')
    for name, price in info:
        print(f"{name}: {price}")


def scrape_page(url, pattern=None, replace_list=None):
    data = []
    if url == '' or url is None:
        raise ValueError('Url cannot be empty')
    while url:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        data += get_data(soup, pattern, replace_list)

        next_page_link = soup.find('a', title='Следваща страница')
        if next_page_link:
            url = next_page_link.get('href')
        else:
            url = None

    return data


def get_data(content, pattern, replace_list):
    # Find the list of item and iterate through each article
    list_results = content.find(id='list-results')
    articles = list_results.find_all('article')

    info = []

    # Extract desk name and price for each article
    for ar in articles:
        title = ar.find(class_='ttl').text
        price = ar.find(class_='price').text.strip()
        name = title

        if pattern is not None:
            match = re.search(pattern, title)
            if match:
                name = match.group(1)

        if replace_list:
            for replace_item in replace_list:
                name = name.replace(replace_item, '')

        info.append((name, price))

    sort_list = sort_info(info)

    return sort_list


def get_info(data, file_path):
    try:
        existing_info = load_existing_info(file_path)

        updated_info = update_info(existing_info, data, file_path)

        if len(updated_info) != len(existing_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        print_info(data)

    except Exception as e:
        print(f"An error occurred: {e}")


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
