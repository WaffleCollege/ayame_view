from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


#この辺はよく分かっていない。データベースは、共通している
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    text = db.Column(db.Text)



#選んだカテゴリーと自分で書いたお題をデータベースに保存する。
@app.post('/debate_page')
def submit_topic():
    category = request.form["category"]#name=categoryのボタンを選択したら、categoryとして保存される。
    text = request.form["free_text"]

    if category:
        # カテゴリーの保存処理
        new_category = Category(category=category)
        db.session.add(new_category)
    if text:
        # 話題の保存処理
        new_topic = Topic(text=text)
        db.session.add(new_topic)
    db.session.commit()


#categoryを選択したら、その場でAIが議題を生成する画面にいくか、議論画面で議題を作るか

#画面遷移
@app.get("/next_page5")#ボタンを押したら次のページに行く、議論開始！という画面を挟んで、ディベート画面へ遷移
def next_page5():
    return render_template("debate_start.html")#("debate.html")それか、そのままチャット画面に遷移するか


if __name__ == '__main__':
    app.run(debug=True)