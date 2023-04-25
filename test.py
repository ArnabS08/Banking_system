import random

import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_data',
    password = 'Appu2008!'
)

### Checks connection
# if connection.is_connected():
#     print('Connected to MySQL database')

cursor = connection.cursor()
addData = ("INSERT INTO data(account_num, pin, first_name, last_name, birth_date, balance) VALUES(%s, %s, %s, %s, %s, %s);")
testQuery = ("SELECT * FROM data")

### Prints database
# cursor.execute(testQuery)
# database = cursor.fetchall()
# for x in database:
#   print(x)



def equal_checker(column, object):
    selectColumn = ("SELECT %s FROM data")
    cursor.execute(selectColumn, column)
    object = cursor.fetchall()
    for x in object:
        if column == "account_num":
            while selectColumn == x[0]:
                global account_num
                account_num = random.randint(100000,999999)
        elif column == "pin":
            global real_pin
            for x in object:
                if int(real_pin) == x[0]:
                    repeat = False
                    found = True
            if found == False:
                print("Wrong PIN")
                print("try again")
