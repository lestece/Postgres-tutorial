import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()


# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "name" column from the "artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 -select only by "ArtistID" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# QUery 5 -select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 -select all tracks where the composer is "Queen" from the "Track" tbl
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# fetch the results(multiple)
results = cursor.fetchall()


# fetch the result(single)
# results = cursor.fetchone()


# close the connection
connection.close()


# print results
for result in results:
    print(result)
