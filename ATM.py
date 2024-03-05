print("""      ****** Welcome to Gan ATM ******
      1. Take out Money
      2. Deposit
      3. Create Acc
      4. Exit""")

a = 0

while True:
    select = input("Enter your selection: ")[0]
    
    if select == "3":
        n = input("Enter Your Name: ")
        a = float(input("Enter your amount: "))
        
        def create_person(name, amount):
            print(f"Creating a new person named {name} with an initial balance of ${amount}")
        create_person(n, a)
        
    elif select == "1":
        take_out = float(input("How much you want to withdraw: "))
        
        def take_cash(take_out, balance):
            if take_out <= balance:
                balance -= take_out
                print(f"You have withdrawn ${take_out}. Your remaining balance is ${balance}")
                return balance
            else:
                print("You have not enough money!")
                return balance
        
        b = take_cash(take_out, a)
        
    elif select == "2":
        dep = float(input("How much do you want to deposit? "))
        
        def deposit(dep, balance):
            balance += dep
            print(f"You have deposited ${dep}. Your new balance is ${balance}")
            return balance
        
        b = deposit(dep, a)
        
    elif select == "4":
        print("Thank you for using Gan ATM. Have a great day!")
        break
        
    else:
        print("Please input valid option")
