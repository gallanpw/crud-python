import MySQLdb as mdb
import sys

try:
	conn = mdb.connect("localhost", "root", "", "crud_python")
	cur  = conn.cursor()
	cur.execute("SELECT VERSION()")
	ver = cur.fetchone()
	print ("Database version : %s" % ver)

except mdb.Error as e:
	print ("Error %d: %s" % (e.args[0],e.args[1]))
	sys.exit(1)

finally:
	if conn:
		conn.close()