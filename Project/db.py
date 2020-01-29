import mysql.connector

password=""
database = "project_keystrole"
def select(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database) #COnnects to DB
	cur = cnx.cursor(dictionary=True) #Creates cursor constructor for executing and returning results(rows) as lists
	cur.execute(q) #Executes query q(Exists in adminform)
	result = cur.fetchall() #Returns result as tuple
	cur.close() #Close DB connection
	cnx.close() #Destroy cursor
	return result
def update(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.rowcount
	cur.close()
	cnx.close()
	return result
def delete(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit() #like git commit
	result = cur.rowcount #Number of rows after operation
	cur.close()
	cnx.close()
def insert(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.lastrowid #Return rowid of last inserted
	cur.close()
	cnx.close()
	return result
def insert(q):
	cnx = mysql.connector.connect(user="root", password=password, host="localhost", database=database)
	cur = cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result = cur.lastrowid
	cur.close()
	cnx.close()
	return result

