import oracledb

def get_connection():
    return oracledb.connect(
        user="YOURUSERNAME",
        password="YOURPASSWORD",
        dsn="HOSTNAME/IP:LISTENERPORT/YOURDB"
    )
