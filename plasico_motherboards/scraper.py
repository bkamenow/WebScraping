from web_scraper import scraper


if __name__ == "__main__":
    base_url = 'https://plasico.bg/komponenti/dynni-platki'

    file_path = 'motherboards.json'

    data = scraper.scrape_page(base_url)

    scraper.get_info(data, file_path)
