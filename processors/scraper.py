from web_scraper import scraper


def get_processors_info(info):
    try:
        existing_info = scraper.load_existing_info(file_path)

        updated_info = scraper.update_info(existing_info, info, file_path)

        if len(updated_info) != len(existing_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        scraper.print_info(info)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    base_url = 'https://plasico.bg/komponenti/procesori'
    pattern = r'(.*?)\s\|'
    file_path = 'processors.json'
    data = scraper.scrape_page(base_url, pattern)
    get_processors_info(data)


