import sqlite3
conn = sqlite3.connect("alerte_infection.db")
cur = conn.cursor()

for table in ["infection", "cas", "lieux"]:
    print(f"\nTable {table}:")
    for row in cur.execute(f"SELECT * FROM {table}"):
        print(row)

conn.close()