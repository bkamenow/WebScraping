# plasico.bg Web Scrapers Collection

## Overview
The plasico.bg Web Scrapers Collection is a repository containing web scrapers tailored specifically for extracting data from plasico.bg, an online store offering a variety of products. These scrapers are built using BeautifulSoup and Requests, and they efficiently extract valuable information from plasico.bg for various purposes.

## Features
- **Scalable**: Each web scraper is capable of handling the unique structure and data format of plasico.bg.
- **Customizable**: Users can easily customize the scrapers to fit their specific requirements by modifying the code.
- **Easy to Use**: The scrapers offer a simple and intuitive interface, making it effortless for users to run and customize them.

## Included Web Scrapers
1. **Gaming Desk Scraper**: Extracts information about gaming desks from plasico.bg, providing details such as desk names and prices.
1. **Gaming Laptops Scraper**: Extracts information about gaming laptops from plasico.bg, providing details such as laptop names and prices.

## Usage
1. **Clone the Repository**:
    ```bash
    git clone git@github.com:bkamenow/WebScraping.git
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Choose a Web Scraper**:
    Navigate to the directory of the desired web scraper (e.g., `plasico_gaming_desks`).

4. **Run the Scraper**:
    Execute the `scraper.py` file to run the web scraper.
    ```bash
    python scraper.py
    ```

5. **View Results**:
    Once the scraper completes, view the extracted data in the output file or console.

## License
This project is licensed under the [MIT License](LICENSE).
