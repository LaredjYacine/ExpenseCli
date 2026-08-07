import argparse


# print('1- add expense')
# print('2- add a new expense category')
# print('3- remove expense')
# print('4- total expense')
# print('5- list expense')
class Expense :
    
    expenses = []  
    def __init__(self,f):

        self.file =f
        try:
            with open(self.file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        
                        if not line or line == "category,amount":
                            continue
                            
                        category, price = line.split(',')
                        
                        self.expenses.append({'category': category, 'amount': price})
                        
        except FileNotFoundError:
            try :
                with open(self.file, 'w')as f :
                    f.write('')
            except FileNotFoundError:
                print(f"Error: The directory or path for '{self.file}' is bad/does not exist.")


    def saveExpense(self):
        try : 
            with open(self.file,'w') as f :
                for e in self.expenses:
                    f.write(f"{e['category']},{e['amount']}\n")
            return True 
        except (FileNotFoundError, OSError) : 
                return False 


    def addExpense(self,category,amount):
        try:
            isin= False
            amount = int(amount) 
            for expense in self.expenses : 
                if expense['category'] == category:
                    isin=True
                    am = expense['amount']
                    expense['amount'] =int(am) +  amount
            if not isin:
                print('your category was not found ')
            else:
                self.saveExpense()
                return True 
        except ValueError:
            print('enter a valid value  ')
        except Exception:
            print('make sure u entered the correct category and amount')
        
    def removeExpense(self,category):
        #self.viewExpenses()
        try:
            category = int(category)
            i = 1
            if category >=1 and category<=len(self.expenses):
                self.expenses.pop(category-1) 
            self.saveExpense()
            return True 
        except ValueError:
            return 'enter a valid value'


    def addAnewExpenseCategory(self,category,amount):
        try:

            self.expenses.append({'category': category , 'amount': amount})
            self.saveExpense()
            return True
        except ValueError: 
            print('enter a valid value')
        except Exception:
            print('make sure u entered the correct category and amount')


    def viewExpenses(self):
        print("Your Expenses :")
        i= 1
        for expense in self.expenses :
            print(f"{i}- {expense['category']} = {expense['amount']}$")
            i+=1


    def totalExpenses(self):
        total_amount = 0 
        for expense in self.expenses: 
            total_amount = total_amount + int(expense['amount'])

        print(total_amount)

