import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proj"
)

cursor1 = db.cursor()
sql1= """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 1
        """

cursor1.execute(sql1)
result1 = cursor1.fetchall()

cursor2 = db.cursor()
sql2= """ 
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 2
        """
cursor2.execute(sql2)
result2 = cursor2.fetchall()

cursor3 = db.cursor()
sql3= """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 3
        """
cursor3.execute(sql3)
result3 = cursor3.fetchall()

cursor4 = db.cursor()
sql4 = """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 4
        """
cursor4.execute(sql4)
result4 = cursor4.fetchall()

cursor5 = db.cursor()
sql5 = """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 5
        """
cursor5.execute(sql5)
result5 = cursor5.fetchall()

cursor6 = db.cursor()
sql6 = """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 6
        """
cursor6.execute(sql6)
result6 = cursor6.fetchall()

cursor7 = db.cursor()
sql7 = """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 7
        """
cursor7.execute(sql7)
result7 = cursor7.fetchall()

cursor8 = db.cursor()
sql8 = """
        SELECT
            episode
        FROM
            shot
        WHERE
            episode = 8
        """
cursor8.execute(sql8)
result8 = cursor8.fetchall()


print("Frame Count Episode 1 :",len(result1))
print("Frame Count Episode 2 :",len(result2))
print("Frame Count Episode 3 :",len(result3))
print("Frame Count Episode 4 :",len(result4))
print("Frame Count Episode 5 :",len(result5))
print("Frame Count Episode 6 :",len(result6))
print("Frame Count Episode 7 :",len(result7))
print("Frame Count Episode 8 :",len(result8))
