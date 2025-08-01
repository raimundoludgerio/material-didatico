from flask import Blueprint, render_template, request, redirect, url_for, session
from utils import load_data, save_data

posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/')
def list_posts():
    posts = load_data('data/posts.json')
    return render_template('posts/list.html', posts=posts)

@posts_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        posts = load_data('data/posts.json')
        new_post = {
            "id": len(posts) + 1,
            "title": request.form['title'],
            "content": request.form['content'],
            "author": session['username']
        }
        posts.append(new_post)
        save_data('data/posts.json', posts)
        return redirect(url_for('posts.list_posts'))

    return render_template('posts/create.html')
