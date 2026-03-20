import oracledb

def get_connection():
    return oracledb.connect(
        user="dbmonitor",
        password="dbmonitor",
        dsn="localhost:1521/ORADB"
    )