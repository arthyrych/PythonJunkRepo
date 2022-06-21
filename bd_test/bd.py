print('Let\'s create a database.\n')

import sqlite3

conn = sqlite3.connect('my_first_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE employee (id_1 INTEGER NOT NULL, 
                                         first_name VARCHAR NOT NULL, 
                                         last_name VARCHAR NOT NULL,
                                         PRIMARY KEY (id_1))
                                         ''')
cursor.execute('''CREATE TABLE salary (id_2 INTEGER NOT NULL, 
                                       salary VARCHAR NOT NULL, 
                                       salary_in_USD VARCHAR NOT NULL,
                                       FOREIGN KEY (id_2) REFERENCES employee (id_1))
                                       ''')
cursor.execute('''CREATE TABLE position (id_3 INTEGER NOT NULL, 
                                         position VARCHAR NOT NULL, 
                                         experience VARCHAR NOT NULL,
                                         FOREIGN KEY (id_3) REFERENCES employee (id_1))
                                         ''')

cursor.close()
conn.close()
