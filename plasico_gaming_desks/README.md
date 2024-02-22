# Gaming Desk Scraper

## Description
The Gaming Desk Scraper is a Python application that scrapes information about gaming desks from a website, updates the existing information stored in a JSON file, and displays any new additions. It is useful for keeping track of the latest gaming desk offerings and their prices.

## Features
- Scrapes gaming desk information from a specified webpage.
- Handles multiple pages of gaming desk listings.
- Updates existing desk information with new entries.
- Stores desk information in a JSON file for future reference.
- Provides feedback on any new additions to the desk listings.

## Installation
1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
- Run the main.py script:
    ```bash
    python main.py
    ```
  The script will scrape gaming desk information from the specified webpage, update the JSON file with any new entries, and display the names and prices of the new desk additions.

## Configuration
- Modify the main.py script to change the URLs of the webpages to scrape.
- Adjust the regular expression patterns in the `get_gaming_desk_info` function to match the desk name format on the website, if necessary.

## Dependencies
- **requests**: For making HTTP requests to fetch webpage content.
- **BeautifulSoup**: For parsing HTML content and extracting data from webpages.
- **json**: For handling JSON data serialization and deserialization.
- **re**: For working with regular expressions.
- **os**: For interacting with the operating system (checking file existence, etc.).

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.
