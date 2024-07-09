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
base_url = 'https://github.com/maymaymay2024/kadai/edit/main/kadai.py/repository/branch/folder_path/'


# Goボタンが押されたとき
if st.button('Go'):
    # 選択された祈願に対応する画像フォルダを決定
    if option == '安産祈願':
        folder_path = os.path.join(base_path, '安産祈願')
    elif option == '金運上昇祈願':
        folder_path = os.path.join(base_path, '金運上昇祈願')
    else:
        folder_path = os.path.join(base_path, '長寿祈願')

    # フォルダ内の画像ファイルを取得
    images = os.listdir(folder_path)
    selected_image = random.choice(images)
    image_path = os.path.join(folder_path, selected_image)

    # 画像を表示
    img = Image.open(image_path)
    st.image(img, caption=selected_image)



    

