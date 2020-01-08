import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proj"
)

mycursor = db.cursor()

#default FPS = 30
query= ("SELECT \
            episode,sum(duration*30) \
        FROM \
            shot \
        GROUP BY \
            episode"
        )

mycursor.execute(query)
result = mycursor.fetchall()

for x in result:
    print(x)