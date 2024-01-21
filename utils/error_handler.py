# error_handler.py

import streamlit as st
import configparser

class ErrorHandler:
    @staticmethod
    def handle_error(error_message, operation):
        try:
            return operation()
        except configparser.NoSectionError:
            st.error("The section was not found in the config.ini file. Please check your configuration.")
        except Exception as e:
            st.error(f"{error_message}: {e}")
