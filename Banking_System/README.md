🏦 Banking System V2

A simple terminal-based Banking System built with Python.
This project simulates basic banking operations such as creating accounts, searching for accounts, depositing money, and withdrawing money.

📌 Features

- 👤 Create one or multiple accounts
- 🔎 Search accounts using account numbers
- 💰 Deposit money
- 💸 Withdraw money
- ✅ Validate positive deposit amounts
- ✅ Prevent withdrawals greater than the current balance
- ✅ Validate menu choices
- 📊 Store account information using dictionaries and a list

🛠️ Concepts Used

- Variables
- Lists
- Dictionaries
- Functions
- "while" loops
- "for" loops
- Conditional statements
- Dictionary keys and values
- List methods
- "return"
- Boolean values
- User input and validation
- f-strings

▶️ How It Works

When the program starts, it displays a menu:

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          Banking system
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
1. Account data
2. Search account
3. Deposit
4. Withdraw
5. Exit

The user selects an operation from the menu.

👤 Account Data

The program collects:

- User name
- Account number
- Initial deposit

Each account is stored as a dictionary:

{
    "user": user,
    "account_number": account_number,
    "current_balance": current_balance
}

Multiple account dictionaries are stored inside the "data" list.

🔎 Search Account

The user enters an account number.

The program searches through the stored accounts and returns the matching account when found.

💰 Deposit

The user searches for an account and enters a deposit amount.

The amount is added to the account's current balance.

💸 Withdraw

The user searches for an account and enters a withdrawal amount.

The program checks that:

- The amount is greater than zero.
- The amount does not exceed the current balance.

If valid, the amount is subtracted from the balance.

💾 Data Storage

Account information is stored temporarily in memory using a Python list containing dictionaries:

data = []

The data is not permanently saved to a file or database. 
It will be lost when the program stops.

🎯 Purpose of the Project

This project was created to practice Python fundamentals and understand how lists, dictionaries, functions, loops, conditions, 
and data validation can be combined to build a more structured terminal application.

👨‍💻 Project Status

Completed — Python Terminal Project

Built as part of my Python project portfolio while learning programming fundamentals.
