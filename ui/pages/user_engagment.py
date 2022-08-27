import streamlit as st
from PIL import Image
import sys, os

path = os.path.dirname(__file__)
path = path+'/../images/'
topusedapps = Image.open(path+'topusedapps.png')

st.write("Top 3 used apps")
st.image(topusedapps, caption='Top 3 used apps')

top10 = Image.open(path+'top10customers.png')
st.write("Top 10 Customers Per engagment metrics")
st.image(top10, caption='Top 3 used apps')

top10freq = Image.open(path+'top10userspersession.png')
st.write("Top 10 Users per session frquency")
st.image(top10freq, caption='Top 3 used apps')

elbow = Image.open(path+'clusters.png')
st.write("Elbow of the cluster")
st.image(elbow, caption='Top 3 used apps')