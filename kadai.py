import streamlit as st
import random
import os
from PIL import Image

# タイトルの設定
st.title('祈願お守り画像')

# 祈願の選択フレーム
option = st.selectbox(
    '祈願の種類を選んでください',
    ('安産祈願', '金運上昇祈願', '長寿祈願')
)

# GitHubリポジトリのベースURL
base_url = 'https://github.com/maymaymay2024/kadai/tree/main/'


# Goボタンが押されたとき
if st.button('Go'):
    # 選択された祈願に対応する画像フォルダを決定
    if option == '安産祈願':
        folder_url = base_url + '安産祈願/'
    elif option == '金運上昇祈願':
        folder_url = base_url + '金運上昇祈願/'
    else:
        folder_url = base_url + '長寿祈願/'

# ランダムに画像を選択
    selected_image = random.choice(images)
    image_url = folder_url + selected_image

    # 画像をダウンロード
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))

    # 画像を表示
    st.image(img, caption=selected_image)

    

