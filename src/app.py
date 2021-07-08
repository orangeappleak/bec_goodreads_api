from flask import jsonify
from flask import Flask

from src.popular_books import getPopularCategories
from src.popular_books import getTopBooks
from src.popular_books import find_book

main_app = Flask(__name__)

@main_app.route('/')
def Home():
    return '''
    <h1>This is a books api</h1>
    <h2>available links</h2>
    <h2>/popularCategories</h2>
    '''


@main_app.route('/popularCategories')
def popular_books():
    return jsonify({
        'popular_book_categories': getPopularCategories()
    })

@main_app.route('/popularCategories/<bookRoute>')
def getBooks(bookRoute):
    return jsonify({
        bookRoute : getTopBooks(bookRoute)
    })

@main_app.route('/<book_url>')
def getBookInfo(book_url):
    return jsonify({
        "bookData": find_book(book_url)
    })