expenses = []
def add_expense():
        expense_name = input("Enter expense name: ")
        
        while expense_name.strip() == "":
            print("Expense name can't be empty.")
            expense_name = input("Enter expense name: ")
        amount = int(input("Enter expense amount: "))
        
        while amount <= 0:
            print("You can't enter expense amount in - or 0")
            amount = int(input("Enter expense amount: "))
        expenses.append([expense_name, amount])    
            
def show_expenses():
    if len(expenses) == 0:
        print("Your expense list is empty")
    else:
        for index, expense in enumerate (expenses, start=1):
            #print(index, expense)
            print(f"{index}. {expense[0]} - ₹{expense[1]}")       

def show_total_expenses():
    total = 0
    for expense in expenses:
        total += expense[1]
    print(total)   

def delete_expense():
    if len(expenses) == 0:
        print("Your expense list is empty!")
        return
        
    show_expenses()
    user = int(input("Enter the expense number which want you delete in your list: "))
    
    while user <1:              
        print("Please enter valid number.")
        user = int(input("Enter the valid expense number: "))
    
    while user >len(expenses) :
        print("Please enter valid number.")
        user = int(input("Enter the valid expense number: "))                       
    removed_expense = expenses.pop(user - 1)
    print(f"Expense removed successfully: {removed_expense[0]} - ₹{removed_expense[1]}")

def main():
    while True:
        print("=" * 40)
        print("          Expense tracker")
        print("=" * 40)
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Show Total Expenses")
        print("4. Delete Expense")
        print("5. Exit")
        user = int(input("Enter your choice: "))
        while user not in [1, 2, 3, 4, 5]:
            print("Invalid choice, please enter a valid choice: ")
            user = int(input("Enter your choice: "))
        if user == 1:
            add_expense()
        elif user == 2:
             show_expenses()
        elif user == 3:
            show_total_expenses()
        elif user == 4:
            delete_expense()                        
        else:
             break                   
main() 