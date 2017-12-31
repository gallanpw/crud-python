import MySQLdb as mdb
import sys

conn = mdb.connect("localhost", "root", "", "crud_python")
cur  = conn.cursor()

try:
	sql = "SELECT * FROM user"
	cur.execute(sql)
	user = cur.fetchall()

	print ("ID", "Nama")
	for val in user:
		# print ("ID : %s" %val[0], "Nama : %s" %val[1])
		print ("%s" %val[0], " %s" %val[1])

except:
	print ("Select Data Gagal")

if conn:
	conn.close()
