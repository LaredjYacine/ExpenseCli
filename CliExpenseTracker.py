file ='text.txt'
print('1- add expense')
print('2- add a new expense category')
print('3- remove expense')
print('4- total expense')
print('5- list expense')



def loadexpenses():
    expenses = []  
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            
            if not line or line == "category,amount":
                continue
                
            category, price = line.split(',')
            
            expenses.append({'category': category, 'amount': price})
            
    return expenses  


def saveExpense(expnse):
    with open(file,'w') as f :
        for e in expnse:
            f.write(f"{e['category']},{e['amount']}\n")

def addExpense(e):
    try:
        isin= False
        category = input('category: ')
        amount = int(input('amount: '))
        for expense in e : 
            if expense['category'] == category:
                isin=True
                am = expense['amount']
                expense['amount'] =int(am) +  amount
        if not isin:
            print('your category was not found ')
        saveExpense(e)
    except ValueError:
        print('enter a valid value ')
    except Exception:
        print('make sure u entered the correct category and amount')
    
def removeExpense(e):
    viewExpenses(e)
    try:
        category= int(input('Enter which line : ').strip())
        i = 1
        if category >=1 and category<=len(e):
            e.pop(category-1) 
        saveExpense(e)
    except ValueError:
        print(' enter a valid value ')


def addAnewExpenseCategory(e):
    try:
        category= input('Enter New category : ')
        amount = input('Enter Amount : ')
        e.append({'category': category , 'amount': amount})
        saveExpense(e)
    except ValueError: 
        print('enter a valid value')
    except Exception:
        print('make sure u entered the correct category and amount')


def viewExpenses(e):
    print("Your Expenses :")
    i= 1
    for expense in e :
        print(f"{i}- {expense['category']} = {expense['amount']}$")
        i+=1


def totalExpenses(e):
    total_amount = 0 
    for expense in e : 
        total_amount = total_amount + int(expense['amount'])

    print(total_amount)


while __name__ =="__main__":


    option = input('choose what operation you want to do: ')
    e= loadexpenses()
    match option.strip(): 
        case '1':
            addExpense(e)
        case '2':
            addAnewExpenseCategory(e)
        case '3':
            removeExpense(e)
        case '4':
            totalExpenses(e)
        case '5':
            viewExpenses(e)
        case _ :
            print('enter a valid option')
