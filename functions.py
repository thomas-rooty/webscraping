import base64
import requests


# Fetch the BDM website using a search parameter
def search_on_bdm(param, page):
  return requests.get('https://www.blogdumoderateur.com/page/' + page + '/?s=' + param)

# Build the dataframe from the returned results
def build_json(search_result):
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
