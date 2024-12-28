#flaskをimport　ここは同じだと思うから後で統合すると思う
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#簡単、普通などの、モード選択ボタンを押したら、次のページに行く
@app.route('/next4page', methods=['POST'])
def next_page4():
    mode = request.form['mode']
    if mode== "easy":
        #AIのプロンプトのモードという部分に、easyだと指示を出したい。
        prompt = f"ディベートのモードは{mode}です。以下の議題について議論してください。"
        # 議題は別の変数や関数から取得する想定→次のcategory選択画面で取得。それらを組み合わせて、元々あるプロンプトに組み込みたい。
        #AIには渡すが、すぐには使わない。
        return render_template('category.html')


