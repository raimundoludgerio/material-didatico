from flask import Blueprint, render_template, request, redirect, url_for
from utils import load_data, save_data

authors_bp = Blueprint('authors', __name__, url_prefix='/authors')

@authors_bp.route('/')
def list_authors():
    authors = load_data('data/authors.json')
    return render_template('authors/list.html', authors=authors)

@authors_bp.route('/create', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        authors = load_data('data/authors.json')
        new_author = {
            "id": len(authors) + 1,
            "username": request.form['username'],
            "password": request.form['password']
        }
        authors.append(new_author)
        save_data('databases/authors.json', authors)
        return redirect(url_for('authors.list_authors'))
    return render_template('authors/create.html')
