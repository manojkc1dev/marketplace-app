# ----- Prerequisite ----- #
# pip3 install mysqlclient
# pip3 install mysql-connector-python
# pip3 install mysql (optional?)
# ------------------------ #

import mysql.connector

import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

# (1)
env_filename = '.env'
dotenv_path = join(dirname(__file__), env_filename)
load_dotenv(dotenv_path)

# (2)
# load_dotenv(find_dotenv())

dataBase = mysql.connector.connect(
    host = os.environ.get('DB_HOST'),
    user = os.environ.get('DB_USER'),
    passwd = os.environ.get('DB_PASSWORD'),
)

dataBase_name = os.environ.get('DB_NAME')

cursorObject = dataBase.cursor()

if dataBase_name:
    cursorObject.execute(f"CREATE DATABASE IF NOT EXISTS {dataBase_name}")
    print("Successfully created database!")
else:
    print("[x] Database name is not provided...")
