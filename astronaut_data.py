import sqlite3
import re

def InsertStatment(CON,CUR,STATMENT_LIST) :

    for statments in STATMENT_LIST :
        CUR.execute(statments)
    CON.commit()

def TableStructure(CUR,TABLE) :
    #Will delete any table nameed astronaut if it exits
    CUR.execute('DROP TABLE IF EXISTS Astronauts')
    CUR.execute(TABLE)


#THIS STATMENT WILL RETURN THE INSERT STATMENTS FOR THE TABLE
def getInsertStatments(F) :
    x = re.compile(r'^INSERT INTO.+;?',re.MULTILINE)
    statments = x.findall(F)
    return statments

#THIS STATMENT WILL RETURN THE TABLE STRUCTURE
def getTableStructure(F) :
    x = re.compile(r'CREATE TABLE.+?;',re.MULTILINE|re.DOTALL)
    table = x.search(F)
    return table.group()

def main() :
    
    conn = sqlite3.connect("astronaut.sqlite")
    cur = conn.cursor()

    fpath = fpath =r'C:\\Users\\Atowar\\Desktop\\py4e\\Database\\Astronaut\\astronauts.sql';
    sql_file = open(fpath);

    TABLE = getTableStructure(sql_file.read())
    TableStructure(cur,TABLE)
    #SET THE FILE POINTER TO ZERO
    if sql_file.tell() > 0 :
        sql_file.seek(0)

    STATMENT_LIST = getInsertStatments(sql_file.read())
    InsertStatment(conn,cur,STATMENT_LIST)

main()
