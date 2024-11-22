Password = "12345"

while True:
    EnterPassword = input("Enter the password to get access")
    if EnterPassword == Password:
        print("correct Password Access Granted")
        break
    else:
        print("Worng Password Access Denied, Please Try Again Later")