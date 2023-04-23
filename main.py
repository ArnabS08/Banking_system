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

"**************************************************************************************"
# def equal_checker(column, object):
#     selectColumn = ("SELECT %s FROM data")
#     cursor.execute(selectColumn, column)
#     object = cursor.fetchall()
#     for x in object:
#         if selectColumn == "account_num":
#             while selectColumn == x:
#                 global account_num
#                 account_num = random.randint(999999999,10000000000)
#         elif selectColumn == "pin":
#             global pin
#             found = False
#             repeat = True
#             for x in object:
#                 if int(pin) == x:
#                     repeat == True
#                     found = True
#             if found == False:
#                 print("Wrong PIN")
#                 print("try again")
            
"**************************************************************************************"
print("\nWelcome to Monke Bank!")

while True:
    log_or_sign = input("\nLogin, sign up, or exit? ")

    if log_or_sign.lower() == "login":
        found = False
        repeat = True
        while repeat == True:
            pin = input("\nPIN: ")
            cursor.execute("SELECT pin FROM data")
            login = cursor.fetchall()
            for x in login:
                if int(pin) == x:
                    repeat = False
                    found = True
            if found == False:
                print("Wrong PIN")
                print("try again")

                
            # pin = input("\nPIN: ")
            # equal_checker("pin", "login")


    elif log_or_sign.lower() == "sign up":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        birth_date = input("Date of birth (YYYY-MM-DD): ")
        pin = int(input("Create PIN: "))
        account_num = random.randint(999999999,10000000000)
 
        cursor.execute("SELECT account_num FROM data")
        accNum = cursor.fetchall()
        for x in accNum:
            while account_num == x:
                account_num = random.randint(999999999,10000000000)

        data = [account_num, pin, first_name, last_name, birth_date, 0.00] # All info is put in a list in this order to put in database
        
        try:
            cursor.execute(addData, data)
            connection.commit() # This commits the new data.

            print(f"New user has been created.\nWelcome {first_name} {last_name}!")

        except:
            connection.rollback() # If an error occured while commiting, this reverses the commit.
            print("There was a problem while creating your account, please try again.")

    elif log_or_sign.lower() == "exit":
        print("Thank you, goodbye!")
        break

    else:
        print("You can only type login in, sign up, or exit.")