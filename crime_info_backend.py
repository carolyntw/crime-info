import sqlite3

def connect():
    conn=sqlite3.connect("crimes.db")
    cur=conn.cursor()
    cur.execute("Create Table IF NOT EXISTS crime (id INTEGER PRIMARY KEY,Type text,Street text,Zipcode integer,Day integer,Month integer,Year integer)")
    conn.commit()
    conn.close()

def insert(Type,Street,Zipcode,Day,Month,Year):
    conn=sqlite3.connect("crimes.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO crime VALUES (NULL,?,?,?,?,?,?)",(Type,Street,Zipcode,Day,Month,Year))
    conn.commit()
    conn.close()   

def view():
    conn=sqlite3.connect("crimes.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM crime")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(Type="",Street="",Zipcode="",Day="",Month="",Year=""):
    conn=sqlite3.connect("crimes.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM crime WHERE Type=? OR Street=? OR Zipcode=? OR Day=? OR Month=? OR Year=?",(Type,Street,Zipcode,Day,Month,Year))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("crimes.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM crime WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,Type,Street,Zipcode,Day,Month,Year):
    conn=sqlite3.connect("crimes.db")
    cur=conn.cursor()
    cur.execute("UPDATE crime SET Type=?, Street=?, Zipcode=?, Day=?, Month=?, Year=? WHERE id=?",(Type,Street,Zipcode,Day,Month,Year,id))
    conn.commit()
    conn.close()

connect()
# insert("Robbery","37 Dr.",90007,27,5,2022)
# delete(3)
update(1,"Harrass","37 Dr.",90007,27,5,2022)
print(view())
print(search(Type="Robbery"))