import requests

# Fetch the BDM website using a search parameter
def search_on_bdm(param, page):
  return requests.get('https://www.blogdumoderateur.com/page/' + page + '/?s=' + param)

# Build the dataframe from the returned results
def build_json(search_result):
  return {
    article.get('id'): {
      'name': article.find('h3').text if article.find('h3') else 'No name available',
      'category': article.find('span').text if article.find('span') else 'No category available',
      'date': article.find('time').text if article.find('time') else 'No date available',
    } for article in search_result.find_all('article')
  }
