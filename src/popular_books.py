import requests
from bs4 import BeautifulSoup

def getPopularCategories():
    categories = []
    url = "https://www.goodreads.com/choiceawards/best-books-2020"

    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    result = soup.find('div',class_="categoryContainer").find_all('div',class_="category")
    for category in result:
        categories.append({
            "category_route" : category.find('a')['href'].split('/')[2],
            "category_name" : category.find('h4',class_="category__copy").text,
            "category_image": category.find('img',class_="category__winnerImage")['src']
        })
    return categories

def getTopBooks(route):
    data = requests.get("https://www.goodreads.com/choiceawards/" + route )
    soup = BeautifulSoup(data.content, 'html.parser')
    result = soup.find('div',class_="pollContents").find_all('div',class_="inlineblock pollAnswer resultShown")

    topBooks = []

    topBooks.append({
        "book_ratings": result[0].find('strong').text,
        "book_name" : result[0].find('div',class_="answerWrapper").find('img')['alt'], 
        "book_image": result[0].find('div',class_="answerWrapper").find('img')['src'],
        "winner_book_desc": soup.find('div',class_="readable stacked gcaBookDescription").text
    })

    for book in result[1:]:
        topBooks.append({
            "book_ratings": book.find('strong').text,
            "book_name" : book.find('div',class_="answerWrapper").find('img')['alt'], 
            "book_image": book.find('div',class_="answerWrapper").find('img')['src']
        })

    return topBooks