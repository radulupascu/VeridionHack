import json
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
#pt accept cookies
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from query_data import query_data

query_data()
# Read company data from the JSON file
with open('jsonCompanies.json', 'r') as file:
    company_data = json.load(file)

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

try:
    # Wait for the cookie consent element to be present
    cookie_consent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#L2AGLb"))
    )

    # Click the cookie consent button
    cookie_consent_button.click()
except Exception as e:
    print("Cookie consent button not found or clickable:", e)


companies_news_titles = {}
count=0
for company in company_data:
    count+=1
    company_name = f"news {company['Company Name']}"
    search_input = driver.find_element("name", "q")
    search_input.clear()  # Clear the search input field
    search_input.send_keys(company_name)
    search_input.send_keys(Keys.RETURN)

    #click news link
    try:
        news_link = WebDriverWait(driver, 0).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".LatpMc.nPDzT.T3FoJb:nth-child(0)"))
        )
        news_link.click()
    except Exception as e:
        pass

    #get all news titles from 1st page
    try:
        article_titles_from_divs = WebDriverWait(driver, 0).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.n0jPhd.ynAwRc.MBeuO.nDgy9d'))
        )
        # for article_title in article_titles_from_divs:
        #     print(article_title.text)
        article_titles = [article_title.text for article_title in article_titles_from_divs]
        companies_news_titles[company_name] = article_titles
        print(len(companies_news_titles))
    except Exception as e:
        pass
    if count == 2:
        break
    time.sleep(1)
json_file_path = 'news_titles.json'

with open(json_file_path, 'w') as json_file:
    json.dump(companies_news_titles, json_file, indent=2)

#search_input = driver.find_element("name", "q")

# Perform a Google search
#.send_keys("alphabet nasdaq news")
#search_input.send_keys(Keys.RETURN)

time.sleep(10000)
driver.quit()