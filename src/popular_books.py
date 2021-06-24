import requests
from bs4 import BeautifulSoup

def getPopularCategories():
    url = "https://www.goodreads.com/choiceawards/best-books-2020"

    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    categories = []
    result = soup.find('div',class_="categoryContainer").find_all('div',class_="category")
    for category in result:
        categories.append({
            "category_name" : category.find('h4',class_="category__copy").text,
            "category_image": category.find('img',class_="category__winnerImage")['src']
        })
    return categories
