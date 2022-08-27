import streamlit as st
from PIL import Image
import sys, os

path = os.path.dirname(__file__)
path = path+'/../images/'
topusedapps = Image.open(path+'top3manu.png')

st.write("Top 3 Handset Manufacturers")
st.image(topusedapps, caption='Top 3 Handset Manufacturers')

top10 = Image.open(path+'top10handsets.png')
st.write("Top 10 Handsets")
st.image(top10, caption='Top 10 Handsets')
