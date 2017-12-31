import MySQLdb as mdb
import sys

conn = mdb.connect("localhost", "root", "", "crud_python")
cur  = conn.cursor()

try:
	sql = "SELECT * FROM user WHERE id = %s" % ('1')
	cur.execute(sql)
	user = cur.fetchone()

	print ("ID", "Nama")
	# print ("ID : %s" %user[0], "Nama : %s" %user[1])
	print ("%s" %user[0], " %s" %user[1])

except:
	print ("Select Data Gagal")

if conn:
	conn.close()