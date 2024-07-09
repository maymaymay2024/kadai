import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

# タイトルの設定
st.title('祈願お守り画像')

# 祈願の選択フレーム
option = st.selectbox(
    '祈願の種類を選んでください',
    ('安産祈願', '金運上昇祈願', '長寿祈願')
)

# 各祈願の画像URLリスト
image_urls = {
    '安産祈願': [
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8470.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8471.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8487.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8488.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8489.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8490.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8491.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8492.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8493.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8494.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/安産祈願/IMG_8472.JPG'
    ],
    '金運上昇祈願': [
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2630.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2633.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2647.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2650.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2654.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2659.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/金運上昇祈願/IMG_2644.JPG'
    ],
    '長寿祈願': [
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2928.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2933.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2938.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2939.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2940.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2944.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2945.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2973.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_3031.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_3038.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_3030.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_8483.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_8484.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_8485.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_8486.JPG',
        'https://raw.githubusercontent.com/maymaymay2024/kadai/main/長寿祈願/IMG_2936.JPG'
    ]
}

# Goボタンが押されたとき
if st.button('Go'):
    # 選択された祈願に対応する画像URLリストを取得
    selected_image_urls = image_urls.get(option, [])

    # ランダムに画像を選択
    if selected_image_urls:
        selected_image_url = random.choice(selected_image_urls)

        # 画像をダウンロード
        response = requests.get(selected_image_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))

            # 画像を表示
            st.image(img, caption=selected_image_url.split('/')[-1])
        else:
            st.error('画像のダウンロードに失敗しました。')
    else:
        st.error('指定された祈願の画像が見つかりません。')
