import streamlit as st
from multiapp import MultiApp
#from apps import home, data_stats
from apps import all_songs

app = MultiApp() 

app.add_app("All_songs",all_songs.app)

#app.add_app("Home", home.app)
#app.add_app("Data Stats", data_stats.app) 

app.run()
