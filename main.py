# ------------------------------
# Step 0: 必要なライブラリをインポートする
import tkinter as tk
import joblib
import numpy as np
# ------------------------------
# Step 1: メインウィンドウを作成する
root = tk.Tk()
root.title("あなたはどの動物に似ている？")
    # Step 1-1: メインウィンドウの背景を淡いグレーにする
root.configure(bg="#f0f0f0")
    # Step 1-2: タイトル部分を作成する（ヘッダーバー）
header_frame = tk.Frame(root, bg="#555555", height=60)
header_frame.grid(row=0, column=0, sticky="ew")
title_label = tk.Label(
    header_frame, text="あなたはどの動物に似ている？", bg="#555555", fg="white", font=("Yu Gothic", 20)
)
title_label.pack(pady=10)
    # Step 1-3: 白い中央のコンテナ（カード風）を作成する
main_frame = tk.Frame(root, bg="white", padx=30, pady=30)
main_frame.grid(row=1, column=0, padx=20, pady=20)

# ------------------------------
# Step 2: 特徴量の変数を初期化する（0〜10、初期値5）
activity_var = tk.IntVar(value=5)
social_var = tk.IntVar(value=5)
curiosity_var = tk.IntVar(value=5)
sleep_var = tk.IntVar(value=8) # （初期値は8時間）
food_var = tk.IntVar(value=5)
independence_var = tk.IntVar(value=5)
clingy_var = tk.IntVar(value=5)
stress_var = tk.IntVar(value=5)
# ------------------------------
# Step 3: 特徴量ごとの行を作成する（ラベル、スライダー、現在値表示）

# --- 活動性
def update_activity_value(value):
    activity_value_label.config(text=value)
activity_label = tk.Label(main_frame, text="活動性")
activity_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=activity_var, command=update_activity_value)
activity_value_label = tk.Label(main_frame, text= str(activity_var.get()))

activity_label.grid(row=0, column=0, padx=10, pady=10)
activity_scale.grid(row=0, column=1, padx=10, pady=10)
activity_value_label.grid(row=0, column=2, padx=10, pady=10)

# --- 社交性
def update_social_value(value):
    social_value_label.config(text=value)
social_label = tk.Label(main_frame, text="社交性")
social_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=social_var, command=update_social_value)
social_value_label = tk.Label(main_frame, text=str(social_var.get()))

social_label.grid(row=1, column=0, padx=10, pady=10)
social_scale.grid(row=1, column=1, padx=10, pady=10)
social_value_label.grid(row=1, column=2, padx=10, pady=10)

# --- 好奇心
def update_curiosity_value(value):
    curiosity_value_label.config(text=value)
curiosity_label = tk.Label(main_frame, text="好奇心")
curiosity_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=curiosity_var, command=update_curiosity_value)
curiosity_value_label = tk.Label(main_frame, text=str(curiosity_var.get()))

curiosity_label.grid(row=2, column=0, padx=10, pady=10)
curiosity_scale.grid(row=2, column=1, padx=10, pady=10)
curiosity_value_label.grid(row=2, column=2, padx=10, pady=10)

# --- 睡眠
def update_sleep_value(value):
    hours = int(value)
    if hours < 4:
        label_text = "4時間未満"
        score = 0
    elif hours > 12:
        label_text = "12時間以上"
        score = 10
    else:
        label_text = hours
        score = (hours - 4) * (10 / 8)

    sleep_value_label.config(text=label_text)
sleep_label = tk.Label(main_frame, text="睡眠時間")
sleep_scale = tk.Scale(main_frame, from_=3, to=13, orient="horizontal", variable=sleep_var, command=update_sleep_value)
sleep_value_label = tk.Label(main_frame, text=str(sleep_var.get()))

sleep_label.grid(row=3, column=0, padx=10, pady=10)
sleep_scale.grid(row=3, column=1, padx=10, pady=10)
sleep_value_label.grid(row=3, column=2, padx=10, pady=10)

#  ---食へのこだわり
def update_food_value(value):
    food_value_label.config(text=value)
food_label = tk.Label(main_frame, text="食へのこだわり")
food_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=food_var, command=update_food_value)
food_value_label = tk.Label(main_frame, text=str(food_var.get()))

food_label.grid(row=4, column=0, padx=10, pady=10)
food_scale.grid(row=4, column=1, padx=10, pady=10)
food_value_label.grid(row=4, column=2, padx=10, pady=10)

# --- 自立性
def update_independence_value(value):
    independence_value_label.config(text=value)
independence_label = tk.Label(main_frame, text="自立性")
independence_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=independence_var, command=update_independence_value)
independence_value_label = tk.Label(main_frame, text=str(independence_var.get()))

independence_label.grid(row=5, column=0, padx=10, pady=10)
independence_scale.grid(row=5, column=1, padx=10, pady=10)
independence_value_label.grid(row=5, column=2, padx=10, pady=10)

# --- 依存傾向
def update_clingy_value(value):
    clingy_value_label.config(text=value)
clingy_label = tk.Label(main_frame, text="依存傾向")
clingy_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=clingy_var, command=update_clingy_value)
clingy_value_label = tk.Label(main_frame, text=str(clingy_var.get()))

clingy_label.grid(row=6, column=0, padx=10, pady=10)
clingy_scale.grid(row=6, column=1, padx=10, pady=10)
clingy_value_label.grid(row=6, column=2, padx=10, pady=10)

# --- ストレス対応力
def update_stress_value(value):
    stress_value_label.config(text=value)
stress_label = tk.Label(main_frame, text="ストレス対応力")
stress_scale = tk.Scale(main_frame, from_=0, to=10, orient="horizontal", variable=stress_var, command=update_stress_value)
stress_value_label = tk.Label(main_frame, text=str(stress_var.get()))

stress_label.grid(row=7, column=0, padx=10, pady=10)
stress_scale.grid(row=7, column=1, padx=10, pady=10)
stress_value_label.grid(row=7, column=2, padx=10, pady=10)

# ------------------------------
# Step 4: 予測関数を定義する
# - joblibでモデルとLabelEncoderを読み込む
model = joblib.load("models/best_model.pkl")
le = joblib.load("models/encoder.pkl")

def predict():
    # --- スライダーの値を取得する
    sleep_raw = sleep_var.get()
    sleep_score = 0 if sleep_raw < 4 else (10 if sleep_raw > 12 else (sleep_raw - 4) * (10 / 8))

    features = np.array([[
        activity_var.get(),
        social_var.get(),
        curiosity_var.get(),
        sleep_score,
        food_var.get(),
        independence_var.get(),
        clingy_var.get(),
        stress_var.get()
    ]])

    # --- モデルで予測する
    pred_index = model.predict(features)[0]
    animal_label = le.inverse_transform([int(pred_index)])[0]

    # --- 結果を表示する（テキスト）
    result_text = f"あなたは「{animal_label}」タイプです！"
    result_label.config(text=result_text)

    # --- 画像を表示する
    image_path = f"images/{animal_label}.png"
    try:
        img = tk.PhotoImage(file=image_path)
        image_label.config(image=img)
        image_label.image = img  # ← 画像が消えないように参照を保持
    except Exception as e:
        image_label.config(text="画像が見つかりません", image="")

# ------------------------------
# Step 5: 「診断する」ボタンを作成する
predict_button = tk.Button(main_frame,
                           text="診断開始",
                           command=predict,
                           bg="lightblue",
                           fg="black")
predict_button.grid(row=9, column=1, pady=20)
# ------------------------------
# Step 6: 結果を表示するウィジェットを作成する
# --- テキスト結果用ラベル
result_label = tk.Label(main_frame, text="", font=("Arial", 16))
result_label.grid(row=10, column=0, columnspan=3, pady=10)

# --- 画像表示用ラベル
image_label = tk.Label(main_frame)
image_label.grid(row=11, column=0, columnspan=3)

# ------------------------------
# Step 7: メインループを開始する
root.mainloop()
