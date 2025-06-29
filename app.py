from flask import Flask, render_template, request
from src.predict import predict_animal

app = Flask(__name__)

# 日文動物名と画像ファイル名
animal_images = {
    "ネコ": "ネコ.png",
    "イヌ": "イヌ.png",
    "パンダ": "パンダ.png",
    "フクロウ": "フクロウ.png",
    "カワウソ": "カワウソ.png",
    "ウサギ": "ウサギ.png",
    "ペンギン": "ペンギン.png"
}

# 特徴名リスト
labels = ['活動性', '社交性', '好奇心', '睡眠時間', '食へのこだわり', '自立性', '依存傾向', 'ストレス対応力']

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_path = None
    input_values = {}

    if request.method == 'POST':
        try:
            # ユーザー入力の値を取得して保存
            input_values = {label: request.form.get(label, '') for label in labels}

            # 睡眠スコアを計算
            sleep_hours = float(input_values['睡眠時間']) if input_values['睡眠時間'] else 8
            if sleep_hours < 4:
                sleep_score = 0
            elif sleep_hours > 12:
                sleep_score = 10
            else:
                sleep_score = (sleep_hours - 4) * (10 / 8)

            # 特徴量を作成
            features = [
                float(input_values['活動性']),
                float(input_values['社交性']),
                float(input_values['好奇心']),
                sleep_score,
                float(input_values['食へのこだわり']),
                float(input_values['自立性']),
                float(input_values['依存傾向']),
                float(input_values['ストレス対応力'])
            ]

            # 予測
            animal = predict_animal(features)
            result = animal
            image_path = "images/" + animal_images.get(animal, "")
        except Exception as e:
            result = "エラーが発生しました"
            image_path = None

    return render_template("index.html", result=result, image_path=image_path, input_values=input_values)
if __name__ == '__main__':
    app.run(debug=True)