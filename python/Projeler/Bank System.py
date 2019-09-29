import os
import time
BankName = "AlTechBank"


class Customer():
    def __init__(self,ID,NAME,PASSWORD):
        self.id = ID
        self.__name = NAME
        self.__password = PASSWORD
        self.__balance = 0
    def getName(self):
        return self.__name
    def getPassword(self):
        return self.__password
    def getBalance(self):
        return self.__balance
    def setBalance(self,amount:int):
        self.__balance += int(amount)

class Bank():
    def __init__(self):
        self.customers = list()

    def beCustomer(self,ID,NAME,PASSWORD):
        os.system("cls")
        self.customers.append(Customer(ID,NAME,PASSWORD))
        print("""
        -- ==  WELCOME TO {}!  == --
        
        Hello, {}
        Your ID Number is {}
        Your Password is {}
        """.format(BankName,NAME,ID,len(PASSWORD)*"*"))

        input("Please press any key...")

def Main():
    counter_ID = 0
    counter_Quit = False
    bank = Bank()

    while True:
        counter_Quit = False
        os.system("cls")
        print("Welcome To {}!".format(BankName))
        print("="*(12+len(BankName)),"\n") # for align
        print("""
[1]: I am a Customer
[2]: I want to be a customer
        """)

        choice_1 = input("Please Select => ")

        if choice_1 == "1":
            ids = [i.id for i in bank.customers]
            os.system("cls")
            while True:
                if counter_Quit == True:
                    break
                TryID = input("Enter Your ID: ")
                if TryID in ids:
                    counter_ID = 0
                    for customer in bank.customers:
                        if customer.id == TryID:
                            TryPassword = input("Enter Your Password: ")
                            if TryPassword == customer.getPassword():
                                while True:
                                    os.system("cls")
                                    print("Welcome {}!".format(customer.getName()))
                                    print((10+len(customer.getName()))*"=","\n")
                                    print("""
                                    [1]: How much is my balance
                                    [2]: Deposit money into my account
                                    [3]: Deposit into someone else's account
                                    [4]: Withdraw money
                                    [0]: Quit
                                    """)
                                    choice_2 = input("Please Select => ")
                                    if choice_2 == "0":
                                        os.system("cls")
                                        print("Thank you for choosing us! Goodbye!")
                                        input("Please press any key...")
                                        counter_Quit = True
                                        break
                                    elif choice_2 == "1": # How much is my balance
                                        os.system("cls")
                                        print("Hi! {}".format(customer.getName()))
                                        print("You Have $ {}".format(customer.getBalance()))
                                        input("Please press any key...")
                                    elif choice_2 == "2": # Deposit money into my account
                                        os.system("cls")
                                        print("Hi! {}".format(customer.getName()))
                                        amount = int(input("Please Enter Amount: "))
                                        print("Previous Balance $ {}".format(customer.getBalance()))
                                        customer.setBalance(amount)
                                        print("Now Balance $ {}".format(customer.getBalance()))
                                        input("Please press any key...")
                                    elif choice_2 == "3": # Deposit into someone else's account
                                        os.system("cls")
                                        print("Hi! {}".format(customer.getName()))
                                        OtherID = input("Please Enter ID: ")
                                        if OtherID in ids:
                                            for OtherID2 in bank.customers:
                                                if OtherID == OtherID2.id:
                                                    amount = input("Please Enter Amount: ")
                                                    if int(amount) > int(customer.getBalance()):
                                                        print("You don't have enough money")
                                                        input("Please press any key...")
                                                    else:
                                                        os.system("cls")
                                                        print("Transfer Successful!")
                                                        print("Previous Balance $ {}".format(customer.getBalance()))
                                                        customer.setBalance(-int(amount))
                                                        OtherID2.setBalance(+int(amount))
                                                        print("Now Balance $ {}".format(customer.getBalance()))
                                                        input("Please press any key...")
                                        else:
                                            print("This id was not found. Please try again")
                                            input("Please press any key...")
                                            continue
                                    elif choice_2 == "4": # Withdraw money
                                        os.system("cls")
                                        amount = input("Please Enter Amount: ")
                                        if int(amount) > int(customer.getBalance()):
                                            print("You don't have enough money")
                                            input("Please press any key...")
                                        else:
                                            print("You Withdraw ${}".format(amount))
                                            print("Previous Balance $ {}".format(customer.getBalance()))
                                            customer.setBalance(-int(amount))
                                            print("Now Balance $ {}".format(customer.getBalance()))
                                            input("Please press any key...")
                            else:
                                print("Password Wrong! Please Try Again")
                                input("Please press any key...")

                else:
                    counter_ID +=1
                    if counter_ID >= 3:
                        print("Please try again later..")
                        time.sleep(2)
                        counter_ID = 0
                        break

                    else:
                        print("This id was not found. Please try again")
                        input("Please press any key...")




        elif choice_1 == "2":
            os.system("cls")
            print("Hello! We are very excited for this moment!")
            print("""                    ===""")
            ids = [i.id for i in bank.customers]

            ID = input("Which ID number do you want? => ")

            if ID in ids:
                print("It is using id number. Please repeat the process")
                input("Please press any key...")
            else:
                NAME = input("What's your name? => ")
                PASSWORD = input("Set Password => ")
                print("")
                bank.beCustomer(ID,NAME,PASSWORD)


        else:
            print("Wrong Choice! Please Try Again..")
            input("Please press any key...")



if __name__ == '__main__':
    Main()