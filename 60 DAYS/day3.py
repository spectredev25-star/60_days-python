#expense tracker program

def getBudget():
    while True:
        budget = input('ESTIMATED BUDGET($): ')
        if budget.isdigit():
            budget = float(budget)
            break
        else:
            print('BUDGET MUST BE A VALID DIGIT.')
    return budget

def getExpense():
    while True:
        expense = input('ESTIMATED EXPENSE($): ')
        if expense.isdigit():
            expense = float(expense)
            break
        else:
            print('BUDGET MUST BE A VALID DIGIT.')
    return expense

def main():
    budget = getBudget()
    expense = getExpense()
    if expense > budget:
        print("OOPS,THAT'S TOO EXTRAVENT")
    elif expense == budget:
        print("WELL, THAT'S A NICE WAY TO SPEND.")
    elif expense < budget:
        print("A LITTLE BIT OF ECONOMIZATION IS A SKILL.")
    else:
        print("OOPS,CAN'T HANDLE THIS.")

if __name__ == '__main__':
    main()