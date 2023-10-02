from collections import namedtuple
import altair as alt
import json
import requests
import streamlit as st
import numpy as np
import pandas as pd
import scikit-learn as sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def app():
    # GitHubのJSONファイルのURL (rawファイルを指定)
    github_url = "https://raw.githubusercontent.com/Taka0007/song-recommendation-apps/main/data/songs.json"

    # JSONデータをGitHubから読み込む
    response = requests.get(github_url)
    if response.status_code == 200:
        karaoke_data = json.loads(response.text)
    else:
        st.error("JSONデータを読み込めません。GitHub URLを確認してください.")
        return

    data = karaoke_data["songs"]
    songs_df = pd.DataFrame(data)
    songs_df['artist_genre'] = songs_df['artist'] + ' ' + songs_df['genre']

    # TF-IDFベクトル化
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(songs_df['artist_genre'])

    # コサイン類似度を計算
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Streamlitアプリのコード
    st.title("曲のおすすめ")

    # 曲名の入力
    input_title = st.text_input("おすすめを受けたい曲のタイトル", "曲 1")

    if st.button("おすすめを表示"):
        # 入力された曲のおすすめを取得
        idx = songs_df[songs_df['title'] == input_title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        song_indices = [i[0] for i in sim_scores]
        recommended_songs = songs_df['title'].iloc[song_indices]

        st.write("おすすめの曲:")
        st.write(recommended_songs)
