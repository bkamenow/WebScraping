from web_scraper import scraper


def get_gaming_laptops_info(info):
    try:
        existing_desk_info = scraper.load_existing_info(file_path)

        updated_info = scraper.update_info(existing_desk_info, info, file_path)

        if len(updated_info) != len(existing_desk_info):
            print("Update message: New information has been added.")
        else:
            print("Nothing new.")

        # print information
        scraper.print_info(info)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    pattern = r'^([^,]+)'

    url = 'https://plasico.bg/laptopi-i-aksesoari/laptopi/filter-F107'

    replace = ['UPGRADED ']

    file_path = 'gaming_laptops.json'

    info = scraper.get_info(url, pattern, replace_list=replace)

    get_gaming_laptops_info(info)
