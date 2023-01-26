import psycopg2

try:
    conn = psycopg2.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = 'ehdjsyd77@')
except psycopg2.DatabaseError as db_err:
    print(db_err)