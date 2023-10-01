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
  
  st.title("カラオケ曲追加")

  # 新しい曲の情報を入力
  new_title = st.text_input("曲名")
  new_artist = st.text_input("アーティスト")
  new_genre = st.text_input("ジャンル")
  new_rating = st.slider("評価", 0.0, 5.0, 2.5, 0.1)

  # 追加ボタンを押して新しい曲を追加
  if st.button("曲を追加"):
      new_song = {
          "title": new_title,
          "artist": new_artist,
          "genre": new_genre,
          "rating": new_rating
      }
      karaoke_data["songs"].append(new_song)

      # カラオケ曲をGitHubのJSONファイルに上書き保存
      response = requests.put(github_url, data=json.dumps(karaoke_data))
      if response.status_code == 200:
          st.success(f"曲 '{new_title}' が追加されました！")
      else:
          st.error("曲を追加できませんでした。GitHub URLを確認してください。")
