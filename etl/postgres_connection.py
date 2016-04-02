import psycopg2

#return RedShift db cursor

def redshift_db(dbname,username,password):
	conn_string = "dbname='"+dbname+"' port='5439' user='" + username + "' password='" + password + "' host='wit-data-cluster.c0osrkcbo2bc.us-west-2.redshift.amazonaws.com'"
	print "Connecting to database\n        ->%s" % (conn_string)
	conn = psycopg2.connect(conn_string)

	return conn

def run_query(cursor,conn,query):
	cursor.execute(query)
	return cursor
