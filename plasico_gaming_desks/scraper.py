from web_scraper import scraper


def get_gaming_desks_info(info):
    try:
        # Load existing desk information from the JSON file
        existing_desk_info = scraper.load_existing_info(file_path)

        # Update existing desk information with new entries
        updated_desk_info = scraper.update_info(existing_desk_info, new_desk_info, file_path)

        # Check if new information has been added
        if len(updated_desk_info) != len(existing_desk_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        # print information
        scraper.print_info(new_desk_info)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url_page1 = 'https://plasico.bg/game-zone/geymyrski-byura'
    url_page2 = 'https://plasico.bg/game-zone/geymyrski-byura/p2'

    file_path = 'gaming_desks.json'
    pattern = r'бюро\s+(.*?)(?=,|\d{3}/\d{2}/\d{2}\sсм)'
    replace = [' с поставка за монитор', ' с регулируема височина', ' с електрическо управление']

    # Get gaming desk information from both pages
    new_desk_info_page1 = scraper.get_info(url_page1, pattern, replace_list=replace)
    new_desk_info_page2 = scraper.get_info(url_page2, pattern, replace_list=replace)

    # Combine desk information from both pages
    new_desk_info = new_desk_info_page1 + new_desk_info_page2

    get_gaming_desks_info(new_desk_info)
