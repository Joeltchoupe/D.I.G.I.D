#this code aims to create a blockchain-based database that's used to store encrypted identification datas and to offer to users functionnalities to access those datas by a decentrailsed way.
# -*- coding: utf-8 -*-
import mysql.connector
#connexion to the database

def create_db():
  db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
  )
#create a database cursor to perform SQL operations
cur = db.cursor()
#
execute the cursor with the execute() method and passed the SQL query
cur.execute("CREATE DATABASE my_db")

#verify if database exists
  cur.execute("SHOW DATABASES")
for x in cur:
  print(x)

#connection to the Msql servers
import mysql.connector
conn = mysql.connector.connect(host="localhost",
                               user="root", password="", 
                               database="db")
cursor = conn.cursor()
conn.close()
-------------------------------------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
import sys
sql_create = """
CREATE TABLE IF NOT EXISTS Users ( 
   index int(6) NOT NULL, 
   name varchar(100) DEFAULT NULL, 
   age int(3) DEFAULT NULL, 
   last_probe_degree float(5,2) DEFAULT NULL, 
   PRIMARY KEY(ref), 
   CHECK (age>=0) ); """
try:
   conn = mysql.connector.connect((host="localhost",
                               user="root", password="", 
                               database="db")
   cursor = conn.cursor()
   cursor.execute(sql_create)
   try:
      index = (554871, "James Cameron", 68, 4.8) 
      cursor.execute("""INSERT INTO Users (index, name, age, last_probe_degree) VALUES(%s, %s, %s, %s)""", reference)
      
      reference = {'ref': 543154, 'nom' : "Michael Jordan", 'age' : 60, 'last_probe_degree' : 3.75} 
      cursor.execute("""INSERT INTO Produits (ref, nom, stock, prix) VALUES(%(ref)d, "%(nom)s", %(stock)d, %(prix)f)""", index)
      conn.commit()
   except:
      # En cas d'erreur on annule les modifications
      conn.rollback()
   cursor.execute("""SELECT ref, nom, prix FROM Produits WHERE stock > %d """, (0, )) 
   rows = cursor.fetchall() 
   for row in rows: 
      print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
except mysql.connector.errors.InterfaceError as e:
   print("Error %d: %s" % (e.args[0],e.args[1]))
   sys.exit(1)
finally:
   # On ferme la connexion
   if conn:
      conn.close()  
