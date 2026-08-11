💰 Expense Tracker

A simple terminal-based Expense Tracker built with Python.
This project allows users to add, view, calculate, and delete expenses through a menu-driven interface.

📌 Features

- ➕ Add a new expense
- 📋 View all saved expenses
- 💵 Calculate total expenses
- 🗑️ Delete an expense
- ✅ Validate expense names
- ✅ Prevent zero or negative expense amounts
- ✅ Validate menu choices
- ✅ Validate expense numbers before deletion

🛠️ Concepts Used

- Variables
- Lists
- Functions
- "while" loops
- "for" loops
- Conditional statements
- "enumerate()"
- List indexing
- "append()"
- "pop()"
- User input and validation
- f-strings

▶️ How It Works

When the program starts, it displays a menu:

========================================
          Expense tracker
========================================
1. Add Expense
2. Show All Expenses
3. Show Total Expenses
4. Delete Expense
5. Exit

The user selects an option to perform an action.

Add Expense

The program asks for:

- Expense name
- Expense amount

It checks that the name isn't empty and that the amount is greater than zero.

Show All Expenses

Displays expenses with their number, name, and amount.

Example:

1. Books - ₹500
2. Snacks - ₹100

Show Total Expenses

Calculates the total amount of all stored expenses.

Delete Expense

The user selects an expense number, and the selected expense is removed from the list.

💾 Data Storage

Expenses are stored temporarily in a Python list:

expenses = []

Each expense is stored as:

[expense_name, amount]

The data exists only while the program is running. It is not permanently saved to a file or database.

🎯 Purpose of the Project

This project was built to practice Python fundamentals and understand how multiple functions, loops, lists, conditions, and input validation can work together to create a complete terminal application.

🚀 Future Improvements

Possible improvements for a future version could include:

- Permanent data storage
- Better input error handling
- Expense categories
- Date tracking
- Search and filtering
- More detailed expense summaries

👨‍💻 Project Status

Completed — Python Terminal Project

Built as part of my Python project portfolio while learning programming fundamentals.
