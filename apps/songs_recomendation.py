from collections import namedtuple
import altair as alt
import json
import requests
import streamlit as st
import numpy as np
import pandas as pd
#import sklearn
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.metrics.pairwise import linear_kernel

def recommend_similar_songs(input_title, songs_df):
    # 入力曲のインデックスを取得
    input_idx = songs_df[songs_df['title'] == input_title].index[0]

    # コサイン類似度を計算
    similarity_scores = []
    for i in range(len(songs_df)):
        if i != input_idx:
            sim_score = np.dot(songs_df.iloc[input_idx, 4:], songs_df.iloc[i, 4:])
            similarity_scores.append((songs_df.iloc[i, 0], sim_score))

    # 類似度に基づいてソート
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # おすすめ曲を取得
    recommended_songs = [song[0] for song in similarity_scores[:5]]
    return recommended_songs


def app():
    # 曲のデータを読み込む
    github_url = "https://raw.githubusercontent.com/Taka0007/song-recommendation-apps/main/data/songs.json"
    response = requests.get(github_url)
    if response.status_code == 200:
        karaoke_data = json.loads(response.text)
    else:
        st.error("JSONデータを読み込めません。GitHub URLを確認してください.")
        return

    # データフレームを作成
    data = karaoke_data["songs"]
    songs_df = pd.DataFrame(data)

    # Streamlitアプリのコード
    st.title("曲のおすすめ")

    # 曲名の入力
    input_title = st.text_input("おすすめを受けたい曲のタイトル", "曲 1")

    if st.button("おすすめを表示"):
        recommended_songs = recommend_similar_songs(input_title, songs_df)
        st.write("おすすめの曲:")
        for song in recommended_songs:
            st.write(song)
