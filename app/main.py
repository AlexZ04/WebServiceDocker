import os
import psycopg2
from fastapi import FastAPI, status
from random import choice
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host='db')
except:
    exit()

app = FastAPI()
cursor = conn.cursor()


@app.get('/test')
def root():
    return {"message": "Test"}


@app.get('/')
def root():
    cursor.execute('SELECT * FROM numbers')
    try:
        numbers = cursor.fetchall()
        return choice(numbers)
    except:
        return status.HTTP_500_INTERNAL_SERVER_ERROR
