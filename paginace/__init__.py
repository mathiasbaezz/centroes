import pymysql
conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'Maherbacpaik1',
    db = 'cefcyt'
)

pymysql.version_info = (1, 4, 0, "final", 0)
pymysql.install_as_MySQLdb()

