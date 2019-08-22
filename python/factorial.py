## started coding 18.07.2019
## finished coding 18.07.2019

number = int(input("Number = ")) ## we get number
factorial = 1 ## we determine the factorial variable

if number < 0: ## if the entered number is not positive
    print("Please input a positive number") 
elif number == 0: ## 0! = 1
    print("Result: 1")
else: ## if the entered number is positive
    for i in range (1,number+1):
        factorial = factorial * i
    print("Result:",factorial)