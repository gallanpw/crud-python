import MySQLdb as mdb
import sys

conn = mdb.connect("localhost", "root", "", "crud_python")
cur  = conn.cursor()

sql = "DELETE FROM user WHERE id = '%s'" % ("6")

try:
	cur.execute(sql)
	conn.commit()
	print ("Delete Data Berhasil")
	print (cur._last_executed)

except:
	conn.rollback()
	print ("Delete Data Gagal")
	print (cur._last_executed)

if conn:
	conn.close()