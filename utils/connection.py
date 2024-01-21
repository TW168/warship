# connection.py

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from datetime import datetime

import configparser

def create_db_engine(section):
    """
    Create a SQLAlchemy engine using the database configuration from a config.ini file.

    Parameters:
    section (str): The name of the section in the config.ini file that contains the database configuration.

    Returns:
    engine: A SQLAlchemy engine for the specified database.
    """
    # Read the config.ini file
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        # Get the mysql credentials
        user = config.get(section, 'user')
        password = config.get(section, 'password')
        host = config.get(section, 'host')
        database = config.get(section, 'database')
    except configparser.NoSectionError:
        print(f"{datetime.now()}: The section '{section}' was not found in the config.ini file.")
        return None

    try:
        # Create the engine
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
        
        # Try to connect to the database
        connection = engine.connect()
        connection.close()
        return engine
    except OperationalError:
        print(f"{datetime.now()}: Could not connect to the database. Please check your configuration.")
        return None
