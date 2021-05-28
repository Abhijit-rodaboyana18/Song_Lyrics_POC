import sys
salary=int(input("enter the salary amount - "))
rem_bal = salary
exp_details = {}
exp_amt = 0

while salary>0:    
    choice =input("If you want to enter expenses -[Y|N] : ")
    if choice=="Y":
        while exp_amt<=salary:
            name=input("Enter Expenditure name - ")           
            amount=float(input("Enter Amount - "))
            exp_amt = exp_amt + amount
            if exp_amt<=salary:
                if name in exp_details.keys():
                    exp_details[name] += amount
                    rem_bal = salary - exp_amt
                else:
                    exp_details[name] = amount
                    rem_bal = salary - exp_amt
                    break
                
            else:
                print("Insufficient Funds")
                print("Available balance - ",rem_bal)
                exp_amt = exp_amt - amount
                break
        else:
            print("Insufficient Funds")
            print("Available balance - ",rem_bal)
            sys.exit()
    elif choice == "N":
        print("Calculations Done!")
        break
    else:
        print("Incorrect Choice")
else:
    print("Salary amount is not valid")
    sys.exit()
    
""" Table Format """
print(f"salary{' '*15}:{' '*15}{salary}/-")
print(f"{'-'*75}")
for k,v in exp_details.items():
    print(f"{k}{' '*16}:{' '*15}{v}")
print(f"{'-'*75}")
print(f"Total{' '*16}:{' '*15}{exp_amt}/-")
print(f"Balance{' '*14}:{' '*15}{rem_bal}/-")

