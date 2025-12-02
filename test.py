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
        print("nice")

name()
        
