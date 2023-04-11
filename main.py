import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank_data',
    password = 'Appu2008!'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM data")
cursor.execute(testQuery)

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
        date_of_birth = input("Date of birth (##/##/####): ")
        print(f"New user has been created.\nWelcome {first_name} {last_name}!")
        break

    else:
        print("You can only type login in, or sign up.")