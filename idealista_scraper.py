from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from idealista_links import nova_construcao
import time
import random
from selenium.webdriver.common.by import By
import re
import csv

options = webdriver.ChromeOptions()

#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

with open('idealista_nova_construcao_listings.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
    # Write the header row
    writer.writerow(["Title", "Price", "Type", "Area", "Floor", "URL"])

    for link in nova_construcao:
        driver.get(link)
        time.sleep(random.uniform(4.3,12.8))

        print(f"Scraping listing for {link}")

        while True:
            
            current_url = driver.current_url

            soup = BeautifulSoup(driver.page_source, "html.parser")
            inside_listing = soup.find_all("div", class_="item-info-container")

            for listing in inside_listing:
            
                title = listing.find("a", class_="item-link")
                title = title.get_text(strip=True) if title else "No title found"

                price = listing.find("span", class_="item-price") 
                price = price.get_text(strip=True).split('€')[0] if price else "No price found"

                details = listing.find_all("span", class_="item-detail")
                detail_texts = [detail.get_text(strip=True) for detail in details]
                print(detail_texts)  # This will print all details as a list

                # If you want to assign these to separate variables:
                type_info = detail_texts[0] if len(detail_texts) > 0 else "N/A"
                area_info = detail_texts[1] if len(detail_texts) > 1 else "N/A"
                floor_info = detail_texts[2] if len(detail_texts) > 2 else "N/A"

                writer.writerow([title, price, type_info, area_info, floor_info, current_url])

            try:
                next_button = driver.find_element(By.XPATH, "//a[@class='icon-arrow-right-after']")
                
                # # Check if 'aria-disabled' is set to 'true' to detect the last page
                if next_button.get_attribute("aria-disabled") == "true":
                    print(f"No more pages for {link}.")
                    break  # Exit the loop if the button is disabled

                # Use a more precise scrolling command to bring the button into view without overshooting
                driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY - 200);", next_button)                
                
                # Use JavaScript to click the next button (bypass overlay issues)
                driver.execute_script("arguments[0].click();", next_button)

                print("Going to the next page")

                # Add a short delay to wait for the page to load
                time.sleep(10)
            
            except Exception as e:
                print(f"Error: {e}")
                break

driver.quit()