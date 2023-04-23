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

print("Welcome to Monkey Bank!")

while True:
    log_or_sign = input("Login in or sign up? ")

    if log_or_sign.lower() == "login in":
        account_num = input("Acount number: ")
        pin = input("PIN: ")
        break

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
            break
        except:
            connection.rollback() # If an error occured while commiting, this reverses the commit.
            print("There was a problem while creating your account, please try again.")

    else:
        print("You can only type login in, or sign up.")