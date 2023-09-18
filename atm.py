# creating a ATM interface using python
#first project in python from octanet internship
 
print("welcome to public bank !!")
pin = 1730
chances = 3
balance = 60000
while chances != 0:
        user_pin = int(input("please enter your pin number:")) # Login phase entering pin number
        if user_pin != pin :
            chances -= 1
            print("wrong pin number")
            print(f"you have {chances} chances left")
        else:
            user_choice = input("B : balance, D : deposit, W : withdraw,H : history") 
            if user_choice == "B" : 
                print(f"your total balance is {balance}")
            if user_choice == "D" :
                deposit_user = int(input("enter the amount that you want to deposit :")) 
                total_balance = deposit_user + balance
                print(f"you have deposited Rs.{deposit_user}")
                print(f"your total balance is{total_balance}")
            if user_choice == "W" :
                withdraw_user = int(input("enter the amount you want to withdraw :")) 
                total_balance = balance - withdraw_user
                print(f"you have withdrawn Rs.{withdraw_user}")
                print(f"your total balance is Rs.{total_balance}")
            if user_choice == "H" :
                history_user = balance
                print(f"last transaction is {history_user}") 
        user_exit = input("would you like to exit? yes/No") 
        if user_exit == "yes" :
            print("Thankyou for using public bank !!")
            break
        else:
            continue