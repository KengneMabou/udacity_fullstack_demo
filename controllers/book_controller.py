from core.app_init import app
from models.book import Book
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from models.sqlalchemy_init import db
import sys
from flask_cors import cross_origin

@app.route('/books/<int:book_id>', methods=['GET', 'PATCH','DELETE'])
#@cross_origin()
def single_book(book_id):
    # OPTIONS requests are automatically implemented and HEAD is also automatically implemented if GET is present.
    if request.method == 'DELETE':
        book = Book.query.filter(Book.id == book_id).one_or_none()
        if book is None:
            # abort(404)
            return jsonify({
                'success': False,
                'error_code': 404,
                'description': 'The book with id {} does not exist'.format(book_id)
            }), 404
        else:
            book.delete()
            return jsonify({
                'success': True,
                'book_id': book_id
            })
    elif request.method == 'PATCH':
        book = Book.query.filter(Book.id == book_id).one_or_none()
        if book is None:
            # abort(404)
            return jsonify({
                'success': False,
                'error_code': 404,
                'description': 'The book with id {} does not exist'.format(book_id)
            }), 404
        else:
            data_sent = request.form or request.get_json()
            book.rating = data_sent.get('rating', '')
            book.update()
            return jsonify({
                'success': True,
                'book': book.format()
            })
    else:
        book = Book.query.filter(Book.id == book_id).one_or_none()
        if book is None:
            # abort(404)
            return jsonify({
                'success': False,
                'error_code': 404,
                'description': 'The book with id {} does not exist'.format(book_id)
            }), 404
        else:
            return jsonify({
                'success': True,
                'book': book.format()
            })

@app.route('/books', methods=['GET','POST'])
# @cross_origin
def get_books():
    # Implement pagination
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        books = Book.query.all()
        formatted_books = [book.format() for book in books]
        return jsonify({
            'success': True,
            'books':formatted_books[start:end],
            'total_books':len(formatted_books)
            })
    else:
        error = False
        new_book = None
        data_sent = request.form or request.get_json()
        try:
            new_book = Book(title = data_sent.get('title', ''),
                            author = data_sent.get('author', ''),
                            rating = data_sent.get('rating', ''),
                            )
            new_book.insert()
        except:
            error = True
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()
            if error == True:
                # abort(400)
                return jsonify({
                    'success': False,
                    'description': 'Database error',
                    'error_code':500,
                }), 500
            else:
                return jsonify(new_book.format())