from web_scraper import scraper

if __name__ == "__main__":
    base_url = 'https://plasico.bg/komponenti/procesori'
    pattern = r'(.*?)\s\|'
    file_path = 'processors.json'
    data = scraper.scrape_page(base_url, pattern)
    scraper.get_info(data, file_path)
