from web_scraper import scraper


if __name__ == '__main__':
    url = 'https://plasico.bg/smartfoni-i-tableti/smartfoni'
    file_path = 'smartphones.json'

    pattern = r'^([^,]+)'

    data = scraper.scrape_page(url, pattern)

    info = scraper.get_info(data, file_path)
