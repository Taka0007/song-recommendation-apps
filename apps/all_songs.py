from collections import namedtuple
import altair as alt
import streamlit as st
import numpy as np
import pandas as pd
import json
import requests

def app():
    # GitHubのJSONファイルのURL (rawファイルを指定)
    github_url = "https://raw.githubusercontent.com/Taka0007/song-recommendation-apps/main/data/songs.json"

    # JSONデータをGitHubから読み込む
    response = requests.get(github_url)
    if response.status_code == 200:
        karaoke_data = json.loads(response.text)
    else:
        st.error("JSONデータを読み込めません。GitHub URLを確認してください.")

    # カラオケ曲一覧のページ
    st.title("カラオケ曲の推薦アプリ")

    # カラオケ曲一覧を表示
    st.write("カラオケ曲一覧:")
    for song in karaoke_data["songs"]:
        st.write(f"曲名: {song['title']}")
        st.write(f"アーティスト: {song['artist']}")
        st.write(f"ジャンル: {song['genre']}")
        st.write(f"評価: {song['rating']}")
        st.write("---")
