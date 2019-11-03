
import psycopg2
import sys

def main():
    
    try:
        con = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='m30w!RAWR'")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS dataLoadMonitor")
        cur.execute("CREATE TABLE dataLoadMonitor(load_id INTEGER PRIMARY KEY, load_description VARCHAR(50), load_start_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, load_end_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)")
        con.commit()
    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
        print("Error %s" % e)
        sys.exit(1)

if __name__ == "__main__":
	main()