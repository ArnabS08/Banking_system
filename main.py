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

print("\nWelcome to Monke Bank!")


"**************************************************************************************"


# def equal_checker(column, object):
#     selectColumn = ("SELECT %s FROM data")
#     cursor.execute(selectColumn, column)
#     object = cursor.fetchall()
#     for x in object:
#         if column == "account_num":
#             while selectColumn == x[0]:
#                 global account_num
#                 account_num = random.randint(100000,999999)
#         else:
#             global real_pin
#             global real_accnum
#             global repeat
#             global found
#             for x in object:
#                 if column == "pin":
#                     if int(real_pin) == x[0]:
#                         repeat = False
#                         found = True
#                 if found == False:
#                     print("Wrong PIN")
#                     print("try again")

#                 elif column == "account_num":
#                     if int(real_accnum) == x[0]:
#                         repeat = False
#                         found = True
#                 if found == False:
#                     print("Wrong Account Number")
#                     print("try again")
            

"**************************************************************************************"
def login():
    found = False
    repeat = True
    while repeat == True:
        global real_pin
        real_pin = input("\nPIN: ")
        cursor.execute("SELECT pin FROM data")
        login = cursor.fetchall()
        for x in login:
            if int(real_pin) == x[0]:
                repeat = False
                found = True
        if found == False:
            print("Wrong PIN")
            print("try again")
        global real_accnum
        real_accnum = input("Account Number: ")
        cursor.execute("SELECT account_num FROM data")
        login = cursor.fetchall()
        for x in login:
            if int(real_accnum) == x[0]:
                repeat = False
                found = True
        if found == False:
            print("Wrong PIN")
            print("try again")

# def login_checker():
#     global repeat
#     global found
#     login = cursor.fetchall()
#     for x in login:
#         if int(real_accnum) == x[0]:
#             repeat = False
#             found = True
#     if found == False:
#         print("Wrong PIN")
#         print("try again")


"**************************************************************************************"


def sign_in():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    birth_date = input("Date of birth (YYYY-MM-DD): ")
    pin = int(input("Create PIN: "))
    account_num = random.randint(100000,999999)

    cursor.execute("SELECT account_num FROM data")
    accNum = cursor.fetchall()
    for x in accNum:
        while account_num == x[0]:
            account_num = random.randint(100000,999999)

    data = [account_num, pin, first_name, last_name, birth_date, 0.00] # All info is put in a list in this order to put in database
    
    try:
        cursor.execute(addData, data)
        connection.commit() # This commits the new data.

        print(f"\nYour account number is {account_num}, you MUST not forget this.")
        print(f"\nNew user has been created.\nWelcome {first_name} {last_name}!")

    except:
        connection.rollback() # If an error occured while commiting, this reverses the commit.
        print("There was a problem while creating your account, please try again.")


"**************************************************************************************"

def main():
    while True:
        log_or_sign = input("\nLogin, sign up, or exit? ")

        if log_or_sign.lower() == "login":
            login()

        elif log_or_sign.lower() == "sign up":
            sign_in()

        elif log_or_sign.lower() == "exit":
            print("Thank you, goodbye!")
            break

        else:
            print("You can only type login in, sign up, or exit.")

main()