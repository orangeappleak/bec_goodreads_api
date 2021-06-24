from flask import jsonify
from flask import Flask

from popular_books import getPopularCategories;

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
