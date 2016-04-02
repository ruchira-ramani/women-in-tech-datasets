from postgres_connection import redshift_db, run_query
from env_settings import *

##Connection
conn = redshift_db(dbname,username,password)
cursor = conn.cursor();







#Captures Column Names 
#column_names = [];
#cursor.execute("Select * from SCHEMA_NAME.TABLE_NAME limit 0;");
#column_names = [desc[0] for desc in cursor.description]
#all_cols=', '.join([str(x) for x in column_names])


#conn.commit();
#conn.close();