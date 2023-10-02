import streamlit as st
from multiapp import MultiApp
#from apps import home, data_stats

# apps配下のディレクトリにアプリを追加した際には、ここのimportに追加をしないとエラーを吐く
from apps import all_songs,add_songs,songs_recomendation

app = MultiApp() 

app.add_app("All_songs",all_songs.app)
app.add_app("Add_songs",add_songs.app)
app.add_app("Song_recommendation",songs_recomendation.app)

#app.add_app("Home", home.app)
#app.add_app("Data Stats", data_stats.app) 

app.run()
