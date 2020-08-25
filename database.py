import random
import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()

def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS malli(name TEXT,age INT)')
create_table()

def Disease():
    c.execute('CREATE TABLE IF NOT EXISTS Disease(Disease TEXT)')
Disease()