import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proj"
)

# if db.is_connected():
#     print("Berhasil Connect !")

cursor = db.cursor()
sql = """
        SELECT 
            project.name,
            episode.name,
            status.name,
            duration
        FROM 
            shot 
        INNER JOIN episode ON shot.episode = episode.id
        INNER JOIN project ON episode.project = project.id
        INNER JOIN status ON shot.status = status.id
        WHERE 
            shot.status = 2
        ORDER BY
            episode.name ASC
        """
cursor.execute(sql)

result = cursor.fetchall()

#print(len(result))
# print('Nama Project, Episode, Status, Duration')
# for data in result:
#     print(len(data))

