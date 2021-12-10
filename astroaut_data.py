import sqlite3
import re

def EmptyDatabase() :
    pass
def InsertStatment(CUR,STATMENT_LIST) :
    pass
def TableStructure(CUR,TABLE) :
    pass

#THIS STATMENT WILL RETURN THE INSERT STATMENTS FOR THE TABLE
def getInsertStatments(F) :
    pass

#THIS STATMENT WILL RETURN THE TABLE STRUCTURE
def getTableStructure(F) :
    x = re.compile(r'CREATE TABLE.+?;',re.MULTILINE|re.DOTALL)
    table = x.search(F)
    return table.group()

def main() :
    fpath = fpath =r'C:\\Users\\Atowar\\Desktop\\py4e\\Database\\Astronaut\\astronauts.sql';
    sql_file = open(fpath);

    TABLE = getTableStructure(sql_file.read())
    print(TABLE)
    #SET THE FILE POINTER TO ZERO
    if f.tell() > 0 :
        f.seek(0)

    #STATMENT_LIST = getInsertStatments(sql_file.read())

main()
