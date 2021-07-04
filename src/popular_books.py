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

def getTopFiction():
    url = "https://www.goodreads.com/choiceawards/best-fiction-books-2020"

    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')

    top_fiction = []

    result = soup.find('div',class_ = "pollContents").find_all('div',class_="inlineblock pollAnswer resultShown")

    for book in result:
        top_fiction.append({
            "book_name": book.find('img')['alt'],
            "book_image": book.find('img')['src'],
            "book_ratings": book.find('strong',class_ ="uitext result").text
        })
    return top_fiction
