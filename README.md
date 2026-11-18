
# 📚 Books to Scrape – Web Scraping Project

## Overview

A Python-based web scraping project that extracts book information from the [Books to Scrape](https://books.toscrape.com/) website using Requests and BeautifulSoup.

The scraper collects book titles, prices, and star ratings across multiple pages and exports the extracted information into a CSV file for further analysis.

## Features

- **Multi-page scraping:** Scrape books from multiple pages by specifying the starting and ending page numbers.
- **Data extraction:** Extract book titles, prices, and star ratings.
- **HTML parsing:** Use BeautifulSoup to parse and navigate HTML content.
- **Error handling:** Handle HTTP request errors and HTML parsing exceptions.
- **CSV export:** Store extracted book information in a CSV file.
- **Append support:** Add new scraped records to an existing CSV file without overwriting previous data.
- **Request delay:** Introduce a one-second delay between requests to avoid sending requests too frequently.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- CSV
- Time
- OS

## Project Structure

```text
books-web-scraper/
│
├── books.csv          # Scraped book data
├── scraper.py         # Main scraping script
└── README.md          # Project documentation
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/books-web-scraper.git
```

### 2. Navigate to the project directory

```bash
cd books-web-scraper
```

### 3. Install the required libraries

```bash
pip install requests beautifulsoup4
```

## Usage

Run the Python script:

```bash
python scraper.py
```

The scraper uses the following function:

```python
scrape_me(start_page=1, end_page=51)
```

You can customize the pages to scrape.

**Examples:**

```python
# Scrape all 50 pages
scrape_me()

# Scrape pages 1 to 10
scrape_me(1, 11)

# Scrape pages 10 to 20
scrape_me(10, 21)

# Scrape pages 25 to 30
scrape_me(25, 31)
```

**Note:** The `end_page` parameter is exclusive because Python's `range()` function does not include the ending value.

## Output

The scraped information is saved in `books.csv`.

The CSV file contains the following columns:

| Column | Description |
|---|---|
| title | Title of the book |
| price | Price of the book |
| rating | Star rating of the book |

### Sample Output

| title | price | rating |
|---|---|---|
| A Light in the Attic | £51.77 | Three stars |
| Tipping the Velvet | £53.74 | One star |
| Soumission | £50.10 | One star |

*Sample data is illustrative.*

## Error Handling

The scraper includes exception handling for:

- HTTP request failures.
- Unsuccessful HTTP responses.
- Missing HTML elements.
- Missing attributes during data extraction.

A timeout is also configured for HTTP requests to prevent waiting indefinitely.

## Future Improvements

Potential enhancements for this project:

- Extract additional book information, such as availability and category.
- Implement automatic retries for failed requests.
- Store scraped data in a database.
- Add logging instead of relying only on print statements.
- Introduce concurrent scraping where appropriate.
- Perform data analysis using Pandas.

## Disclaimer

This project uses [Books to Scrape](https://books.toscrape.com/), a website specifically designed for practicing web scraping.

It is intended for educational purposes.

## Author

**Nuwan Thuduwage Don**


