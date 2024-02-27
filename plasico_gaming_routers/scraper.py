from web_scraper import scraper


def get_gaming_routers_info(info):
    try:
        existing_routers_info = scraper.load_existing_info(file_path)

        updated_routers_info = scraper.update_info(existing_routers_info, info, file_path)

        if len(updated_routers_info) != len(existing_routers_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        scraper.print_info(info)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    url = 'https://plasico.bg/game-zone/ruteri'
    file_path = 'gamin_routers.json'
    pattern = ''
    replace = []

    data = scraper.scrape_page(url)

    get_gaming_routers_info(data)
