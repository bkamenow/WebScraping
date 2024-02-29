from web_scraper import scraper

if __name__ == '__main__':
    url = 'https://plasico.bg/laptopi-i-aksesoari/laptopi/filter-F107'
    file_path = 'gaming_laptops.json'
    pattern = r'^([^,]+)'
    replace = ['UPGRADED ']

    data = scraper.scrape_page(url, pattern, replace)

    scraper.get_info(data, file_path)
