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


    # フォルダ内の画像ファイルを取得
    images = os.listdir(folder_path)
    selected_image = random.choice(images)
    image_path = os.path.join(folder_path, selected_image)

    # 画像を表示
    img = Image.open(image_path)
    st.image(img, caption=selected_image)



    

