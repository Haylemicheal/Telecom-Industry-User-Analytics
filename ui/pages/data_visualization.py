import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from scripts.dataloader import DataLoader
from scripts.visualization import Visualization
def hist(df):
    plot = Visualization(df)
    plot.draw_hist()

def density(df):
    plot = Visualization(df)
    plot.draw_density_plot((1,1))

def scatter(df):
    plot = Visualization(df)
    plot.draw_scatter()

def box(df):
    plot = Visualization(df)
    plot.draw_box_plots()

dl = DataLoader('../data', 'clean_data.csv')
df = dl.read_csv()
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df = df.select_dtypes(include=numerics)
option = st.selectbox(
     'Select a column to View',
     df.columns)

graph = st.selectbox(
     'Select a plot',
     ["Histogram", "Density", "Scatter","Box"])
st.set_option('deprecation.showPyplotGlobalUse', False)
if graph == "Histogram":
    st.pyplot(hist(df[option]))
elif graph == "Density":
    st.pyplot(density(df[option]))
elif graph == "Box":
    st.pyplot(box(df[option]))
elif graph == "Scatter":
    st.pyplot(scatter(df[option]))


