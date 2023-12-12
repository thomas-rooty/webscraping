import base64
import requests
import pandas as pd
from time import sleep
from selenium.webdriver.common.by import By


# Fetch the BDM website using a search parameter
def search_on_bdm(param, page):
  return requests.get('https://www.blogdumoderateur.com/page/' + page + '/?s=' + param)


# Fetch the Cdiscount website using a search parameter
def search_on_cdiscount(param):
  return requests.get('https://www.cdiscount.com/search/10/' + param + '.html#_his_')


# Build the dataframe from the returned results
def build_json_bdm(search_result):
  return {
    article.get('id'): {
      'name': article.find('h3').text if article.find('h3') else 'No name available',
      'link': article.find('a').get('href') if article.find('a') else 'No link available',
      'img': article.find('img').get('src') if article.find('img') else 'No image available',
      'category': article.find('span').text if article.find('span') else 'No category available',
      'date': article.find('time').text if article.find('time') else 'No date available',
    } for article in search_result.find_all('article')
  }


# Function that downloads the dataframe as a CSV file
def download_csv(df):
  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()
  href = f'<a href="data:file/csv;base64,{b64}" download="bdm.csv">Download CSV file</a>'
  return href


# Read the dataframe from the server
def read_bdm_df():
  return pd.read_json('dataframe.json')


# Collect dentists data
def collect_dentists(browser, num_pages, search_city):
  all_dentists = []
  for page in range(1, num_pages + 1):
    # Construct the URL for each page
    page_url = f"https://www.doctolib.fr/dentiste/{search_city}?page={page}"
    browser.get(page_url)

    # Wait for the page to load
    sleep(3)

    # Find all practitioners on the current page
    practiciens = browser.find_elements(By.CLASS_NAME, "dl-search-result-presentation")

    for elem in practiciens:
      try:
        # Get info about the dentist
        name = elem.find_element(By.TAG_NAME, "h3").text
        photo = elem.find_element(By.TAG_NAME, "img").get_attribute("src")
        addresse = elem.find_element(By.TAG_NAME, "span").text

        all_dentists.append({
          "name": name,
          "photo": photo,
          "addresse": addresse
        })
      except Exception as e:
        print(f"Error on page {page}: {e}")

  return all_dentists
