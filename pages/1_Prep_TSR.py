# 1_Prep_TSR.py
import pandas as pd 
import streamlit as st 



st.set_page_config(
    page_title="Prep TSR", 
    page_icon=None,
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={'About':"# CFP Warehouse and Shipping"}
                   )

st.write("Prep TSR")
def upload_and_read_pickup_report():
    """
    This function uploads a file using Streamlit's file_uploader and reads it into a pandas DataFrame.
    The file should be an AmTopp Current Pickup Detail Report in Excel format.

    Returns:
        file_name (str): The name of the uploaded file.
        file_size (int): The size of the uploaded file in bytes.
        df (DataFrame or None): The uploaded file read into a pandas DataFrame, or None if no file was uploaded or if the file type is unsupported.
    """
    df = None  # Initialize df
    file_name = None  # Initialize file_name
    file_size = None  # Initialize file_size

    uploaded_file = st.file_uploader("Choose a AmTopp Current Pickup Detail Report", type= ["xlsx", "xls"], key='data_uploader')
    if uploaded_file is not None:
        # Get the file name
        file_name = uploaded_file.name
        
        # Get the file size
        file_size = uploaded_file.size

        # Read the file into a pandas DataFrame
        if '.xlsx' in file_name or '.xls' in file_name:
            df = pd.read_excel(uploaded_file)
        else:
            st.write("Unsupported file type. Please upload an Excel file.")

    return file_name, file_size, df  # Return file_name, file_size, and df


file_name, file_size, df = upload_and_read_pickup_report()

if df is not None:
    st.write(df)
else:
    st.write("No file uploaded.")
 