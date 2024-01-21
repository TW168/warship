# Summary.py
from utils.connection import create_db_engine
from utils.error_handler import ErrorHandler
import pandas as pd 
from sqlalchemy import text
import streamlit as st


st.set_page_config(
    page_title="Summary", 
    page_icon=None,
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={'About':"# CFP Warehouse and Shipping"}
                   )

st.write('Summary')
engine = ErrorHandler.handle_error("Failed to create DB engine", lambda: create_db_engine('db3'))

query = text("SELECT * FROM ipg_ez")
df = ErrorHandler.handle_error("Failed to execute query", lambda: pd.read_sql_query(query, engine))
st.write(df)

query = text("SELECT DISTINCT Site FROM ipg_ez") 
sites = ErrorHandler.handle_error("Failed to execute query", lambda: pd.read_sql_query(query,engine))
st.write(sites)

query = text("SELECT DISTINCT Product_Group FROM ipg_ez") 
product_group = ErrorHandler.handle_error("Failed to execute query", lambda: pd.read_sql_query(query,engine))
st.write(product_group)

