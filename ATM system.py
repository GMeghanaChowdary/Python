def atm_system():
    balance = 1000
    pin = "1234"
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == pin:
        while True:
            print("\nATM Menu:")
            print("1. View Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                print(f"Your balance is ${balance}")
            elif choice == 2:
                deposit = float(input("Enter deposit amount: "))
                balance += deposit
                print(f"Deposited ${deposit}. New balance is ${balance}")
            elif choice == 3:
                withdrawal = float(input("Enter withdrawal amount: "))
                if withdrawal <= balance:
                    balance -= withdrawal
                    print(f"Withdrew ${withdrawal}. New balance is ${balance}")
                else:
                    print("Insufficient funds")
            elif choice == 4:
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Incorrect PIN. Try again.")
atm_system()
