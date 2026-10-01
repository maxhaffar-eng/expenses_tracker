expenses_input = input("enter your expenses like food:12, transport:20, coffee:5 ")
expenses_list = expenses_input.split(",")

total = 0
for item in expenses_list:
    name, amount = item.split(":")
    amount = float(amount)
    total = total + amount
    print(name, "costs", amount)

print("total expenses:", total)