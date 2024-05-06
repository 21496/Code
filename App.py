#docstring- Zac Newman- airplane database application
#imports
import sqlite3

#constants and variables
DATABASE = "fighters.db"

#functions
def print_all_aircraft():
    """print all the aircrafts nicely"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    for fighter in 
    print(results)
    db.close()

#main code
print_all_aircraft()