from web_scraper import scraper


if __name__ == '__main__':
    url = 'https://plasico.bg/game-zone/ruteri'
    file_path = 'gamin_routers.json'
    pattern = ''
    replace = []

    data = scraper.scrape_page(url)

    scraper.get_info(data, file_path)
