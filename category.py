from flask import Blueprint, request, render_template, redirect, url_for
from extensions import db
from models import AllDebate

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.route('/category_selection', methods=['GET'])
def category_selection():
    categories = ['環境問題', '教育', '社会問題', 'テクノロジー']
    return render_template('category.html', categories=categories)

@category_bp.route('/submit_category', methods=['POST'])
def submit_category():
    category = request.form.get('category')
    debate = AllDebate.query.first()
    if debate:
        debate.category = category
        db.session.commit()
    return redirect(url_for('debate.debate'))

@category_bp.route('/submit_topic', methods=['POST'])
def submit_topic():
    category = request.form.get('category')
    free_text = request.form.get('free_text')

    # データベースに保存する処理
    new_debate = AllDebate(category=category, text=free_text)
    db.session.add(new_debate)
    db.session.commit()

    return redirect(url_for('debate.debate'))  # debate.debateにリダイレクト