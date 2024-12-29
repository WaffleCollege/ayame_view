from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    text = db.Column(db.Text)

@app.route('/debate_page', methods=['POST'])
def submit_data():
    category = request.form['category']
    text = request.form['free_text']
    new_data = Data(category=category, text=text)
    db.session.add(new_data)
    db.session.commit()
    return "データが保存されました"

@app.route("/next_page5", method ="GET")#ボタンを押したら次のページに行く、議論開始！という画面を挟んで、ディベート画面へ遷移
def next_page5():
    return render_template("debate_start.html")#それか、そのままチャット画面に遷移するか


if __name__ == '__main__':
    app.run(debug=True)