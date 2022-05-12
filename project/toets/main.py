import db_functions

conn = db_functions.connect('127.0.0.1', 'root', '', 'porsche', '3306')

# auteur : Tijmen van Jaarveld 
# studentid: 10093257
# datum: 19-04-2022



f = open('porsches.csv', 'r')
regels = f.readlines()
teller = 0
for regel in regels:
    if not teller == 0:
        deel_regel = regel.split(';')
        id = db_functions.insert_type(conn, deel_regel[0],deel_regel[1], deel_regel[2], deel_regel[3])
        db_functions.insert_technical_details(conn, deel_regel[4],deel_regel[5],deel_regel[6],deel_regel[7], id)
    else:
        teller += 1
