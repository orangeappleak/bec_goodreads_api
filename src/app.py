from flask import jsonify
from flask import Flask

from popular_books import getPopularCategories
from popular_books import getTopBooks
from popular_books import find_book

main_app = Flask(__name__)


@main_app.route('/favicon.ico')
def favicon():
    return '''
        <img src="https://www.goodreads.com/favicon.ico" />
    '''

@main_app.route('/')
def Home():
    return '''
    <h1>This is a books api</h1>
    <h2>available links</h2>
    <h2>/popularCategories</h2>
    <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
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
        'book_data': find_book(book_url)
    })