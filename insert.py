import MySQLdb as mdb
import sys

conn = mdb.connect("localhost", "root", "", "crud_python")
cur  = conn.cursor()

sql = "INSERT INTO user (id,nama) VALUE ('%s', '%s')" % (6, "Marjinal")

try:
	cur.execute(sql)
	conn.commit()
	print ("Input Data Berhasil")
	print (cur._last_executed)

except:
	conn.rollback()
	print ("Input Data Gagal")
	print (cur._last_executed)

if conn:
	conn.close()