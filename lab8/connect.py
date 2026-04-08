from config import config
import psycopg2

conn = psycopg2.connect(**config)
cur = conn.cursor()

print("Connected successfully")