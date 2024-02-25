from web_scraper import scraper


def get_gaming_desks_info(info):
    try:
        # Load existing desk information from the JSON file
        existing_desk_info = scraper.load_existing_info(file_path)

        # Update existing desk information with new entries
        updated_desk_info = scraper.update_info(existing_desk_info, info, file_path)

        # Check if new information has been added
        if len(updated_desk_info) != len(existing_desk_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        # print information
        scraper.print_info(info)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = 'https://plasico.bg/game-zone/geymyrski-byura'
    file_path = 'gaming_desks.json'
    pattern = r'бюро\s+(.*?)(?=,|\d{3}/\d{2}/\d{2}\sсм)'
    replace = [' с поставка за монитор', ' с регулируема височина', ' с електрическо управление']

    data = scraper.scrape_page(url, pattern, replace)

    get_gaming_desks_info(data)
