
import sqlite3

def AddD(a,b,c1,c2,d,e):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")
    #print("table created")

    cur.execute("INSERT INTO Doctors values(?,?,?,?,?,?)",(a,b,c1,c2,d,e))

    cur.close()
    conn.commit()
    conn.close()
def DelD(a):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("DELETE FROM Doctors WHERE Name=?",(a,))

    cur.close()
    conn.commit()
    conn.close()
def ViewD():
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("select * from Doctors ")
    row = cur.fetchall()
    return row

    '''cur.close()
    conn.commit()
    conn.close()'''
def AddA(a, b, c, d):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("INSERT INTO Appointments values(?,?,?,?)",(a, b, c, d))

    cur.close()
    conn.commit()
    conn.close()
def DelA(a):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("DELETE FROM Appointments WHERE Name=?", (a,))

    cur.close()
    conn.commit()
    conn.close()
def ViewA():
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("select * from Appointments")
    row = cur.fetchall()
    print(row)
    return row

    '''cur.close()
    conn.commit()
    conn.close()'''
def AddP(a, b, c, d):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("INSERT INTO Patients values(?,?,?,?)", (a, b, c, d))

    cur.close()
    conn.commit()
    conn.close()
def DelP(a):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("DELETE FROM Patients WHERE Name=?", (a,))

    cur.close()
    conn.commit()
    conn.close()
def ViewP():
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("select * from Patients ")
    row = cur.fetchall()
    return row

    '''cur.close()
    conn.commit()
    conn.close()'''
def QueryPw(a):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("select Ward_no from Patients where Name=?",(a,))
    row = cur.fetchall()
    return row

    '''cur.close()
    conn.commit()
    conn.close()'''

def QueryPd(a):
    conn = sqlite3.connect(database="Hospital.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Doctors(Name TEXT PRIMARY KEY, Department TEXT,OPD_Timing_from INTEGER ,Timing_to INTEGER ,Room_no INTEGER ,Phone_no INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Appointments(Name Text PRIMARY KEY, Doctor TEXT,Timing INTEGER ,Phone_no INTEGER )")
    cur.execute("CREATE TABLE IF NOT EXISTS Patients(Name Text PRIMARY KEY,Ward_no INTEGER, Disease TEXT,Doctor TEXT )")

    cur.execute("select Disease,Doctor from Patients where Name=?",(a,))
    row = cur.fetchall()
    return row

    '''cur.close()
    conn.commit()
    conn.close()'''