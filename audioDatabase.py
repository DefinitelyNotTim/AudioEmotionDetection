import mysql.connector

audioDB = mysql.connector.connect(
    host = "localhost",
    user = "Papa T.",
    passwd = "lo0plo0p"
    )

print(audioDB)
