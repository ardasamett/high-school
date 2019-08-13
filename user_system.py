## 16.07.2019 started coding
## 17.07.2019 finished coding
## ===================================
## 18.07.2019 -> comment lines added

admin_username = "root"
admin_password = "toor"
username = "arda"
password = "123"
secretquestion = "code"

def help():
    print(" -- HELP --")

print("""
     ===============
    WELCOME TO SERVICE
    
    -> [1]: Login
    -> [2]: If you've not account, create new
    -> [3]: I forgot my password
    -> [4]: I forgot my username
    -> [5]: I forgot my Secret Question 
    -> [6]: Contact
    -> [8]: Help
    -> [9]: Quit  
    """)

while True:
    raw1 = input("=>>")

    if raw1 == "9": #: QUİT
        print("Thanks for using the service..")
        quit()
    elif raw1 == "1": #: LOGİN
        print("-- LOGIN --")
        try_username = input("Username: ")
        try_password = input("Password: ")
        if (try_username == username) & (try_password == password):
            print("Login Succesful")
            print("Welcome,",username)
            break
        else:
            print("Login unsuccessful")
    elif raw1 == "2": # REGISTER
        print("-- NEW ACCOUNT --")
        try_admin_username = input("Admin Username: ")
        try_admin_password = input("Admin Password: ")
        if (try_admin_username == admin_username) & (try_admin_password == admin_password):
            print("Login Succesful")
            username = input("input username: ")
            password = input("input password: ")
        else:
            print("Login Unsuccesful")
    elif raw1 == "3": # FORGOT PW
        print("-- I FORGOT MY PASSWORD --")
        try_username = input("Username: ")
        try_secretquestion = input("Secret Question: ")
        if (try_username == username) & (try_secretquestion == secretquestion):
            print("Great!",username)
            secretquestion = input("New Secret Question: ")
            print("Okay!")
        else:
            print("Wrong! Please try again")
    elif raw1 == "4": # FORGOT USERNAME
        print("if you forgot your username, please contact to us")
        print("Mail: __will be replaced___")
        print("Phone: __will be replaced___")
        print("Website: __will be replaced___")
    elif raw1 == "5": # FORGOT SQ
        print("-- I FORGOT MY SECRET QUESTIONS --")
        try_username = input("Username: ")
        try_password = input("Password: ")
        if (try_username == username) & (try_password == password):
            secretquestion = input("input new Secret Questions: ")
            print("Great!", username)
        else:
            print("Wrong! Please try again")
    elif raw1 == "6":
        print("Mail: __will be replaced___")
        print("Phone: __will be replaced___")
        print("Website: __will be replaced___")
    elif raw1 == "8":
        help()