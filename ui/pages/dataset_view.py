import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from scripts.dataloader import DataLoader

dl = DataLoader('../data', 'clean_data.csv')
df = dl.read_csv()

st.write(df.head(10))