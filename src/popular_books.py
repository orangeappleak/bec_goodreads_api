import requests
from bs4 import BeautifulSoup

def getPopularCategories():
    categories = []
    url = "https://www.goodreads.com/choiceawards/best-books-2020"

    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')
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
    soup = BeautifulSoup(data.content, 'lxml')
    result = soup.find('div',class_="pollContents").find_all('div',class_="inlineblock pollAnswer resultShown")

    topBooks = []

    topBooks.append({
        "book_ratings": result[0].find('strong').text,
        "book_name" : result[0].find('div',class_="answerWrapper").find('img')['alt'], 
        "book_image": result[0].find('div',class_="answerWrapper").find('img')['src'],
        "book_url": soup.find("span",class_="cover").find("a")['href'],
        "winner_book_desc": soup.find('div',class_="readable stacked gcaBookDescription").text
    })

    for book in result[1:]:
        topBooks.append({
            "book_ratings": book.find('strong').text,
            "book_name" : book.find('div',class_="answerWrapper").find('img')['alt'], 
            "book_image": book.find('div',class_="answerWrapper").find('img')['src'],
            "book_url": book.find('a',class_="pollAnswer__bookLink")['href']
        })

    return topBooks

def find_book(url):
    print(url)
    data = requests.get('https://www.goodreads.com/book/show/' + url)
    soup = BeautifulSoup(data.content,'lxml',from_encoding="utf-8")
    result = soup.find('div',{"class": "leftContainer"})
    right_data = soup.find('div',class_="rightContainer")

    genres = right_data.find_all('div',class_="elementList")

    reviews = soup.find('div',class_="leftContainer").find('div',{"id": "other_reviews"}).find('div',{"id": "reviews"}).find('div',{"id": "bookReviews"}).find_all('div',class_="friendReviews")

    try:
        author_desc = right_data.find('div',class_="bookAuthorProfile__about").find_all('span')
        if len(author_desc) > 1:
            author_desc =author_desc[1].text
        else:
            author_desc = author_desc[0].text
    except  AttributeError:
        author_desc = []


    bookInfo = [{
        "book_name": result.find('h1',{"id":"bookTitle"}).text,
        "book_url": url,
        "books_desc": result.find('div',{"id":"description"}).find_all("span")[1].text,
        "book_image": result.find('img',{"id":"coverImage"})['src'],
        "book_rating_value": result.find('span',{'itemprop': 'ratingValue'}).text,
        "book_ratings": result.find('div',id="bookMeta").find('a',class_="gr-hyperlink").text,
        "about_author": {
            "author_name": right_data.find("div",class_="bookAuthorProfile__name").find('a').text,
            "author_profile_image": right_data.find('div',class_="bookAuthorProfile__photo")['style'],
            "author_follower_count": right_data.find('div',class_="bookAuthorProfile__followerCount").text,
            "author_profile_desc": author_desc
        },
        "book_genres": [],
        "community_reviews": []
    }]

    for genre in genres:
        bookInfo[0]['book_genres'].append(genre.find('div',class_="left").find('a').text)

    for review in reviews:
        try:
            full_book_review = review.find('div',class_="left bodycol").find('div',class_="reviewText stacked").find('span',class_="readable").find_all('span')[1].text
        except IndexError:
            full_book_review = []

        try:
            review_likes = review.find('span',class_="likeItContainer").find('span',class_="likesCount").text
        except:
            review_likes = "no likes"

        bookInfo[0]["community_reviews"].append({
            "book_review": {
                "book_reviewer_name": review.find('a',class_="left imgcol")['title'],
                "book_reviewer_image": review.find('img')['src'],
                "book_review_content_stacked": review.find('div',class_="left bodycol").find('div',class_="reviewText stacked").find('span',class_="readable").find_all('span')[0].text,
                "book_review_content_full" : full_book_review,
                "review_likes": review_likes,
            }
        })
    
    
    return bookInfo

def getNewArticles():

    articleInfo = []

    data = requests.get('https://www.goodreads.com/news?ref=nav_brws_news')
    soup = BeautifulSoup(data.content,'lxml',from_encoding='utf-8')
    result = soup.find('div',class_="newsColumn").find_all('div',class_="elementListLast")

    for article in result[1:]:
        articleInfo.append({
            "article_title": article.find('div',class_="editorialCard__body--right").find('div',class_="editorialCard__title").find('a').text,
            "article_url": article.find('div',class_="editorialCard__body--right").find('div',class_="editorialCard__title").find('a')['href'],
            "article_body": article.find('div',class_="editorialCard__body--right").find('div',class_="editorialCard__body").text,
            "article_timeStamp": article.find('div',class_="editorialCard__body--right").find('div',class_ ='editorialCard__info').find('small',class_="editorialCard__timestamp").find('a').text,
            "article_image": article.find('div',class_="editorialCard__image--left").find('a').find('img')['src'],
        })

    return articleInfo

def mostRead():

    mostReadBooks = []

    data  = requests.get("https://www.goodreads.com/book/most_read")
    soup = BeautifulSoup(data.content,'lxml',from_encoding = 'utf-8')
    mostRead = soup.find('div',class_="leftContainer").find('table',class_="tableList").find_all('tr')

    for tr in mostRead:
        mostReadBooks.append({
            "book_name": tr.find('a',class_="bookTitle").text,
            "book_url": tr.find('a',class_="bookTitle")['href'],
            "book_image": tr.find('img',class_="bookCover")['src'],
            "book_author": tr.find('a',class_="authorName").find('span').text,
        })
        
    return mostReadBooks
