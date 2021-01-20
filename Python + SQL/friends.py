import sqlite3
conn = sqlite3.connect("my_friends.db")

#Create cursor object
c = conn.cursor()

#Execute sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

#Commit changes
conn.commit()

conn.close()