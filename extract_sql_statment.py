import re

def main() :
    fpath =r'C:\\Users\\Atowar\\Desktop\\py4e\\Database\\Astronaut\\astronauts.sql';
    f = open(fpath);

    x = re.compile(r'CREATE TABLE.+?;',re.MULTILINE|re.DOTALL)
    Structure = x.search(f.read())
    #Print the table Structure
    print(Structure.group())

    #set file pointer to the begining of the file
    if  f.tell() > 0  :
        f.seek(0)

    #THIS WILL FIND ALL THE INSERT statments
    x = re.compile(r'^INSERT INTO.+;?',re.MULTILINE)
    INSERT_STATMENTS = x.findall(f.read())
    for STATMENTS in INSERT_STATMENTS :
        print(STATMENTS)


main()
