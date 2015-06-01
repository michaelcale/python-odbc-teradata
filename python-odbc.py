#!/usr/bin/python
# USE python FILENAME USERID PASSWORD
import pyodbc
import sys

userid   = ''
password = ''

userid   = str(sys.argv[1])
password = str(sys.argv[2])

connstr = 'DRIVER=[Teradata];DBCNAME=YOURDBC;Authentication=LDAP;UID=' + userid + ';PWD=' + password + ';DATABASE=YOURDATABASE'

try:
    conn = pyodbc.connect(connstr)
except:
    print 'unable to connect to database'
    
csr = conn.cursor()

sql = 'SELECT CURRENT_TIMESTAMP'

csr.execute(sql)

print csr.fetchone()

csr.close()
del csr
conn.close()
