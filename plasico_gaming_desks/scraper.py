from web_scraper import scraper


if __name__ == "__main__":
    url = 'https://plasico.bg/game-zone/geymyrski-byura'
    file_path = 'gaming_desks.json'
    pattern = r'бюро\s+(.*?)(?=,|\d{3}/\d{2}/\d{2}\sсм)'
    replace = [' с поставка за монитор', ' с регулируема височина', ' с електрическо управление']

    data = scraper.scrape_page(url, pattern, replace)

    scraper.get_info(data, file_path)