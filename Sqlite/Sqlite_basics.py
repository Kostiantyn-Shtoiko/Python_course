import sqlite3

db = sqlite3.connect("first.db")

# Create Cursor
cursor = db.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS  first (
#                 title text,
#                 full_text text,
#                 views integer,
#                 authors text
# )""")
# ============================
# Add
# cursor.execute("INSERT INTO first VALUES ('TikTok is cool!', 'TikTok is realy cool', 23422, 'Admin')")
# ============================
# Search
# cursor.execute("SELECT * FROM first")
# print(cursor.fetchall())

# cursor.execute("SELECT title FROM first")
# print(cursor.fetchall())

cursor.execute("SELECT rowid, * FROM first WHERE views > 50 ORDER BY views DESC ")
items = cursor.fetchall()
# print(cursor.fetchmany(1))
# print(cursor.fetchone())

for item in items:
    print(item[1] + "\n" + item[4])


# ============================
# Delete
# cursor.execute("DELETE FROM first WHERE rowid = 2")
# print(cursor.fetchall())

# ============================
# Data change
cursor.execute("UPDATE first SET authors = 'LLaf' WHERE title = 'TikTok is cool!'")

db.commit()
db.close()