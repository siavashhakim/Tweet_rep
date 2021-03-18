# tip: pip install mysql-connector-python and pip uninstall mysql-connector
import mysql.connector
password = 'Aa1367haksia13852020'

con = mysql.connector.connect(host='localhost',
                                      database='twitterdb', user='root', password=password,auth_plugin='mysql_native_password')