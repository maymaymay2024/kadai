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

# GitHubリポジトリのベースURL
api_base_url = 'https://api.github.com/repos/maymaymay2024/kadai/contents/'

# Goボタンが押されたとき
if st.button('Go'):
    # 選択された祈願に対応する画像フォルダを決定
    if option == '安産祈願':
        folder_url = api_base_url + '安産祈願'
    elif option == '金運上昇祈願':
        folder_url = api_base_url + '金運上昇祈願'
    else:
        folder_url = api_base_url + '長寿祈願'

    # GitHub APIを使用してフォルダ内の画像ファイルリストを取得
    response = requests.get(folder_url)
    if response.status_code == 200:
        files = response.json()
        images = [file['download_url'] for file in files if file['name'].lower().endswith(('.png', '.jpg', '.jpeg'))]

        # ランダムに画像を選択
        if images:
            selected_image_url = random.choice(images)

            # 画像をダウンロード
            response = requests.get(selected_image_url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))

                # 画像を表示
                st.image(img, caption=selected_image_url.split('/')[-1])
            else:
                st.error('画像のダウンロードに失敗しました。')
        else:
            st.error('指定されたフォルダに画像ファイルがありません。')
    else:
        st.error(f'フォルダの内容を取得できませんでした。URLを確認してください。 (ステータスコード: {response.status_code})')
