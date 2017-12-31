import MySQLdb as mdb
import sys

conn = mdb.connect("localhost", "root", "", "crud_python")
cur  = conn.cursor()

sql = "UPDATE user SET nama = '%s' WHERE id = '%s'" % ('Supriadi', 2)

try:
	cur.execute(sql)
	conn.commit()
	print ("Update Data Berhasil")
	print (cur._last_executed)

except:
	conn.rollback()
	print ("Update Data Gagal")
	print (cur._last_executed)

if conn:
	conn.close()