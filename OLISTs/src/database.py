import sqlite3
import pandas as pd

conn = sqlite3.connect("OLISTs/database/olist.db")

conn.execute("PRAGMA foreign_keys = ON")


def run_sql(query):
    return pd.read_sql(query, conn)