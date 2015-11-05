import sqlite3
import os

def read3D3S(file):
    ''' read '''
    
    if os.path.isfile('3d3s.db'):
        print('exist,delete')
        os.remove('3d3s.db')
        
    conn=sqlite3.connect('3d3s.db')
    c_=conn.cursor()
    c_.execute('''CREATE TABLE UNIT( Force TEXT, Length TEXT, Energy TEXT, Tempture TEXT)''')
    c_.execute('''CREATE TABLE MATERIAL( 
            Num INTEGER,      Name TEXT,      Type TEXT,       matClass TEXT
            E   REAL,       Miu  REAL,      C   REAL,        Rou    REAL,     FY  REAL,
            matConc TEXT)''')
    c_.execute('''CREATE TABLE SECTION( 
            TypeNo  INTEGER,    Name TEXT,      Type TEXT,      Para TEXT)''')    
    c_.execute('''CREATE TABLE Node( No INTEGER,    x REAL,     y REAL,     z REAL)''')            
