def name():
    name = input("Please re-enter the name: ")
    if ((len(name) < 2) or (len(name) > 50)):
        print("Name should atleast be 2 characters long or less than 50 characters")
    else:
        relationship()

def relationship():
    relationship = int(input("Please enter relationship to the household Head: \n" 
                         "1 - Head \n" 
                         "2 - Spouse \n" 
                         "3 - Son \n" 
                         "4 - Daugther \n" 
                         "8 - Other Relative \n" 
                         "9 - Other non-lative \n"))
    if relationship != (1 or 2 or 3 or 4 or 8 or 9):
        print("Invalid Number")
        relationship()
    
    else:
        age()

def age():
    age = int(input("Please Enter Age: "))
    if age < 0:
        print("Invalid Number")
    elif age > 150:
        print("Invalid Number")
    else:
        sex()

def sex():
    sex = input("Sex(M/F): ")
    if sex != ("M" or "F"):
        print("Invalid Input.")
    else:
        employmentStatus()
    
def employmentStatus():
    employmentStatus = int(input("Are you 0(Unemployed) or 1(Employed): "))
    if employmentStatus != (0 or 1):
        print("Invalid Input.")
    
    elif employmentStatus == 0:
        salary = 0
    
    else: 
        salary()
    
def salary():

    salary = float(input("What is your monthly salary? "))
    if (salary >= 1000.00) or (salary <= 500000.00):
        return
    else:
        print("Invalid Salary??")
        
    

        
