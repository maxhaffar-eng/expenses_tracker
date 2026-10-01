def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    
    with open("expenses.txt", "a") as file:
        file.write(name + ":" + str(amount) + "\n")
    
    print("Saved!")

def show_total():
    total = 0
    with open("expenses.txt", "r") as file:
        for line in file:
            name, amount = line.strip().split(":")
            amount = float(amount)
            total += amount
            print(name, "-", amount)
    print("Total:", total)

while True:
    choice = input("\n1. Add expense\n2. Show total\n3. Exit\nChoose: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_total()
    elif choice == "3":
        break