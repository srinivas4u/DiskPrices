import streamlit as st
import pandas as pd
from datetime import datetime
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

# Set page configuration
page_title = "Prices Minder"
st.set_page_config(
    page_title=page_title,
    page_icon="shark",  # You can use an emoji or a URL to an image
    layout="wide",
    initial_sidebar_state="auto",
)

# Inject custom HTML for meta tags
description = "Prices Minder"
keywords = "Prices Minder"
st.markdown(f"""
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
""", unsafe_allow_html=True)

# Inject custom CSS for font size and table styles
st.markdown("""
    <style>
        .reportview-container .main .block-container {
            font-size: 10px;
            max-width: 100%;
            margin-left: 0;
            margin-right: auto;
        }
    </style>
""", unsafe_allow_html=True)
