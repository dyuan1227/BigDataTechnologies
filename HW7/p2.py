import sqlite3
from urllib.request import urlopen
import requests
import pandas as pd

#Definening URLs
friends_url="https://snap.stanford.edu/data/facebook_combined.txt.gz"
people_url="https://people.cam.cornell.edu/md825/names.txt"

#Read URLs into Python
people=pd.read_csv(people_url,header=None)
friend=pd.read_csv(friends_url,header=None)

#Convert the format so that they can be pushed to the SQL
people_tuple=[tuple(i) for i in people.to_numpy()]
friend_tuple=[tuple(map(int,i[0].split(" "))) for i in friend.values.tolist()]



# Connecting to the database file
conn = sqlite3.connect('p2.db')
c = conn.cursor()

#Creating table for people/pushing the data into the table
c.execute("DROP TABLE IF EXISTS people")
c.execute('''CREATE TABLE people (personId INTEGER,name text)''')
c.executemany('INSERT INTO people VALUES (?,?)', people_tuple)

#Creating table for friends/pushing the data into the table
c.execute("DROP TABLE IF EXISTS friends")
c.execute('''CREATE TABLE friends (personId1 INTEGER,personId2 INTEGER)''')
c.executemany('INSERT INTO friends VALUES (?,?)', friend_tuple)

#SQL Query that querys NumOfFriends
pd.set_option('display.max_rows', None)
print(pd.read_sql_query("Select Name as Name, Count(PersonId1) as NumOfFriends From (Select personId1 From friends UNION ALL Select PersonId2 From friends) As P JOIN people on P.personId1=people.PersonId Group by Name Order by NumOfFriends DESC",conn))
#Committing changes and closing the connection to the database file


conn.commit()
conn.close()