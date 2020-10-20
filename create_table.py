import sqlite3

cursor.execute('''CREATE TABLE SCHOOL
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         MARKS          INT);''')
         
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (1, 'Rohan', 14, 'Delhi', 200)");
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (2, 'Allen', 14, 'Bangalore', 150 )");
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (3, 'Martha', 15, 'Hyderabad', 200 )");
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (4, 'Palak', 15, 'Kolkata', 650)");

conn.commit()
conn.close()
         
