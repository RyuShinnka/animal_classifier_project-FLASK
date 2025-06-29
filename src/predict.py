import joblib as jl

# モデルとエンコーダーはグローバルに一度だけ読み込む
model = jl.load("models/best_model.pkl")
le = jl.load("models/encoder.pkl")

def predict_animal(X):
    """
    入力: X = [活動性, 社交性, 好奇心, 睡眠時間, 食べ物へのこだわり, 自立性, 甘えん坊度, ストレス耐性]
    出力: 動物名（例: "ネコ"）
    """
    y = model.predict([X])
    y_real = le.inverse_transform(y)
    return y_real[0]
