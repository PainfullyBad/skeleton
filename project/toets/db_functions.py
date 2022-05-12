import mysql.connector

def connect(h,u,p,d,prt:3306):
    try:
        return mysql.connector.connect( host=h
                                    ,   user=u
                                    ,   password=p
                                    ,   database=d
                                    ,   port=prt)
    except mysql.connector.Error as err:
        return err.error

def insert_type(conn, b,t,toe, j):
    sql = f"insert into type (brand, type, toevoeging, jaar) values ('{b}','{t}','{toe}','{j}');"
    cursor = connection.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor = conn.cursor()

    cursor.execute("SELECT LAST_INSERT_ID();")

    result = cursor.fetchone()

    print (result)

    return result[0]

def insert_technical_details(conn, a,i,aa,m,id):
    sql = f"insert into technical_details (aantal_cyl, inhoud_motor, aantal_pk, max_snelheid, type_id) values ({a}, '{i}','{aa}', '{m}',{id});"
    cursor = connection.cursor()
    cursor.execute(sql)
    conn.commit()

