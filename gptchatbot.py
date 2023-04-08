import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

mydb = mysql.connector.connect(
    host = "cloud.mindsdb.com",
    user = os/environ.get("USER"),
    password = os/environ.get("PASSWORD"),
    port = "3306"
)

cursor = mydb.cursor()
cursor.execute('''SELECT response from mindsdb.jacksocrates_model WHERE author_username = "mindsdb AND text = "Who is the best opera singer?"''')

for x in cursor:
    print(x)
