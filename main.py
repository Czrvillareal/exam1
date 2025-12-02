import sqlite3
import sys
import test

with sqlite3.connect("exam_db.db") as connection:
    cur = connection.cursor()


householdHeadName = input("Enter the name of the household head: ")
cur.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table' AND name=?;""", (householdHeadName,))

tableExists = bool(cur.fetchone())

if tableExists == False:
    # print(tableExists)
    cur.execute("CREATE TABLE "+householdHeadName+
                "(ID int NOT NULL, Name varchar(50), Relationship int(1), Age int(3), Employment_Status int(1), Monthly_Salary float(6,2), PRIMARY KEY(ID) )"
                )
# else:
#     cur.execute()

numberOfHouseholdMembers = int(input("Enter the number of household members: "))

listOfHouseholdMembers = []
for i in range(numberOfHouseholdMembers):
    listOfHouseholdMembers.append(input("Enter household member name starting with Household Head: ")) 
    
answer1 = input("Do you want to add more members? 1 - Yes / 2 - No: ")
if answer1 == "1":
        answer2 = int(input("How many more do you want to add?"))
        for i in range(answer2):
            listOfHouseholdMembers.append(input("Enter extra household member name: ")) 
        else:
            print(listOfHouseholdMembers)
            test.name()
        
elif answer1 == "2":
    
    print(listOfHouseholdMembers)
    for i in range(len(listOfHouseholdMembers)):
        print("Enter the following information for Household Member(left to right):")
        test.name()
else:
    print("Invalid Input.")

cur.execute("INSERT INTO "+householdHeadName+" VALUES "+name+" "+relationship+" "+age+" "+sex+" "+employmentStatus+" "+salary+" ")

# print(listOfHouseholdMembers)
