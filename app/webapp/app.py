import os
import streamlit as st
from PIL import Image

# Number of columns for the gallery
num_cols = 3

st.title("MRI Tumor Detection Model App")

images = st.file_uploader("Upload image", type=['png', 'jpg'], accept_multiple_files=True)

models = st.radio(
    "Select A model",
    ['Xception', 'Inception V3','Custom CNN'],
    0
)

