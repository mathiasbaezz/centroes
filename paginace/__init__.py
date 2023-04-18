import pymysql
conn = pymysql.connect(
    host = 'http://168.90.176.4:888/phpmyadmin_f295f2133405ff4a/index.php',
    port = 888,
    user = 'sql_centroes_fct',
    passwd = '8WwetLxjtWs3ms2j',
    db = 'sql_centroes_fct'
)
pymysql.version_info = (1, 4, 0, "final", 0)
pymysql.install_as_MySQLdb()