import streamlit as st 


st.set_page_config(
    page_title="Prep TSR", 
    page_icon=None,
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={'About':"# CFP Warehouse and Shipping"}
                   )

st.write("Prep TSR")
upload_data = st.expander('Upload Data', expanded=True)
upload_data.file_uploader('Select Daily Shipping Report',accept_multiple_files=False)

 