import streamlit as st

st.set_page_config(page_title="Aplikasi Belanja", page_icon="🛒")

st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
	
    .judul-app {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #C71585;
        margin-top: 10px;
        margin-bottom: 30px;
    }
    .menu-box {
        background: linear-gradient(to right, #ffe4ec, #fcd2e2);
        padding: 20px;
	      color: #C71585;
        border-radius: 12px;
        border-left: 6px solid #FF69B4;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }
    .metric-box {
        background-color: #ffe9f0;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        text-align: center;
        color: #C71585;
    }
    .box-shadow {
        background-color: #fffafc;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        border-radius: 10px;
        padding: 15px;
	      color: #C71585;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)
