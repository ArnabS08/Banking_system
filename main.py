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
addData = ("INSERT INTO data(account_num, pin, name, birth_date, balance) VALUES(%s, %s, %s, %s, %s);")
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

def balance_finder(real_accnum):
    balanceFinder = (f"SELECT balance FROM data WHERE account_num = {real_accnum}")
    cursor.execute(balanceFinder)
    global balance
    balance = float(cursor.fetchone()[0])


"**************************************************************************************"


def deposit(real_accnum):
    while True:
        try:
            deposit_num = float(input("\nAmount of deposit: "))
            break
        except:
            print("You can only input a number.")

    balance_finder(real_accnum)
    deposit_num = balance + deposit_num
    deposit = (f"UPDATE data SET balance ={deposit_num} WHERE account_num = {real_accnum}")
    cursor.execute(deposit)
    connection.commit()
    print(f"${deposit_num - balance} has been deposited")
    print(f"You now have ${deposit_num}")

"**************************************************************************************"


def withdraw(real_accnum):
    while True:
        try:
            withdrawal_num = float(input("\nAmount of withdrawal: "))
            break
        except:
            print("You can only input a number.")

    balance_finder(real_accnum)
    withdrawal_num = balance - withdrawal_num
    withdraw = (f"UPDATE data SET balance ={withdrawal_num} WHERE account_num = {real_accnum}")
    cursor.execute(withdraw)
    connection.commit()
    print(f"\n${balance - withdrawal_num} has been withdrew")
    print(f"You now have ${withdrawal_num}")


"**************************************************************************************"


def login():
    found1 = False
    # found3 = False
    repeat = True
    while repeat == True:
        # Checks if any PIN in the database is equal to the PIN that was input.
        real_pin = int(input("\nPIN: "))
        cursor.execute("SELECT pin FROM data")
        pins = cursor.fetchall()
        for x in pins:
            if real_pin == x[0]:
                found1 = True

        if found1 == True:
            # Checks if any account number in the database is equal to the account number that was input.
            real_accnum = int(input("Account number: "))
            accFinder = (f"SELECT account_num FROM data WHERE pin={real_pin}")
            cursor.execute(accFinder)
            accountNums = (cursor.fetchone()[0]) # fetchs one data and takes the first index from the tuple ex: takes the 111111 from (111111,)
            if real_accnum == accountNums:
                nameFinder = (f"SELECT name FROM data WHERE account_num = {real_accnum}")
                cursor.execute(nameFinder)
                print_name = (cursor.fetchone()[0])

                balance_finder(real_accnum)

                print(f"\nWelcome {print_name}!\nYou have ${balance} in your account.")
                repeat = False
            else:
                print("\nWrong account number.")
                print("Please try again.")
        else:
            print("\nWrong PIN.\nPlease try again.")

    while True:
        d_or_w = input("\nWould you like to deposit or withdraw? ")
        if d_or_w.lower() == "deposit":
            deposit(real_accnum)
        elif d_or_w.lower() == "withdraw":
            withdraw(real_accnum)
        else:
            print("You can only type deposit or withdraw.\nPlease try again")


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
    name = input("Name: ")
    birth_date = input("Date of birth (YYYY-MM-DD): ")
    pin = int(input("Create PIN: "))
    account_num = random.randint(100000,999999)

    cursor.execute("SELECT account_num FROM data")
    accNums = cursor.fetchall()
    for x in accNums:
        while account_num == x[0]:
            account_num = random.randint(100000,999999)

    data = [account_num, pin, name, birth_date, 0.00] # All info is put in a list in this order to put in database
    
    try:
        cursor.execute(addData, data)
        connection.commit() # This commits the new data.

        print(f"\nYour account number is {account_num}, you MUST not forget this.")
        print(f"\nNew user has been created.\nWelcome {name}!")

    except:
        connection.rollback() # If an error occured while commiting, this reverses the commit.
        print("There was a problem while creating your account.\nplease try again.")


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
            print("You can only type login in, sign up, or exit.\nPlease try again")

main()