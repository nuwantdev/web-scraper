# import neccessary modules
import requests
import csv
import time
from bs4 import BeautifulSoup


def scrape_me(start_page=1, end_page=51)-> None:
    """
    Scrape books page by page and save the results to a CSV file.
    """
    headers = ["title","price","rating"]
    book_data = []
    with open('books.csv','w', encoding='utf-8', newline='') as file:
        
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        
        for i in range(start_page,end_page):
            url = f'https://books.toscrape.com/catalogue/page-{i}.html'
            print(f"Scraping page {i}: {url}")
            try:
                response = requests.get(url, timeout=10)
            
                if response.status_code != 200:
                    raise Exception(f"Request failed with the status code: {response.status_code}")
                    
                
            
                html_soup = BeautifulSoup(response.content,'html.parser')
                books = html_soup.find_all('article',class_='product_pod')
                
                
           
                for book in books:
                    title = book.h3.a['title']
                    price = book.find('p',class_='price_color').text
                    rating = book.find('p')['class'][1]
                    book_info = {
                        "title":title,
                        "price":price,
                        "rating":f"{rating} stars"
                        }
                    book_data.append(book_info)
                print(f"Scraping page {i} complete!. Waiting 2 second....")
                print("--------------------------------------------------")
                time.sleep(2)
                
            except Exception as e:
                print(e)
                
        writer.writerows(book_data)
        print(f"Scrapping comoleted successfully!. Found {len(book_data)} books. Check books.csv")
        
    
    
    





scrape_me(1,10)