data = []

def account_data():
    while True:
        user = input("Enter your name: ")
        account_number = int(input("Enter your account number: "))
        current_balance = int(input("Enter the amount you want to deposit: "))
        while current_balance <=0 :
            print("Please enter a positive amount.")
            current_balance = int(input("Enter your initial deposit: "))        
        print(f"Your amount ₹{current_balance} is successfully deposited in your account number {account_number}.")            
        accounts_info = {
        "user" : user,
        "account_number" : account_number,
        "current_balance" : current_balance
        }            
        data.append(accounts_info)                             
        add_account = input("Do you want to create more accounts? Enter yes/no: ")
        
        if add_account == "yes":
            continue
        elif add_account == "no":
            break         
    return user, account_number, current_balance, data
#user, account_number, current_balance, data = account_data()

def search_account():
    user = int(input("Enter the account number you want to search: "))
    found = False
    for i in data:
        if user == i["account_number"]:
            print(i)            
            found = True
            print("Account found")
            return i
    if found == False:
        print("Account not found!")
#search_account()  

def deposit_money():
    account = search_account()
    amount = int(input("Enter your deposit amount: "))
    
    while amount <=0 :
        print("InvalidSyntax, please re-enter your deposit amount.")
        amount = int(input("Enter your deposit amount: "))
    print("√Your amount deposited successfully!")
    account["current_balance"] += amount
    #print(account)                                              

def withdraw():
     account = search_account()     
     amount =int(input("Enter, how much ₹ do you want to withdraw: "))
     
     while amount <= 0 or amount > account["current_balance"]:
         print("Please enter a valid amount.")
         print(f"Your current balance is ₹{account['current_balance']}. Please enter an amount less than or equal to that.")
         amount = int(input("Enter, how much ₹ do you want to withdraw: "))
     print("√Your amount withdrawal successfully!")
     account["current_balance"] -= amount
     #print(account)                           

def main():
    while True:
        print("$" * 40)
        print("          Banking system")
        print("$" * 40)
        print("1. Account data")
        print("2. Search account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        client = int(input("Select what you want to do from the given list: "))
        while client not in [1, 2, 3, 4, 5]:
            print("Something went wrong. Please try again.")
            client = int(input("Select the number what you want to do from the given list: "))
        if client == 1:
            account_data()
        elif client == 2:
            search_account()
        elif client == 3:
            deposit_money()
        elif client == 4:
            withdraw()
        elif client == 5:
            print("Thank you for visiting our app.")
            break
        else:
             print("Something went wrong. Please try again.")
main()                                                                                 