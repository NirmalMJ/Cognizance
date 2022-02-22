#Defining the table
tbl = [["Roll Number", "Name", "\tMarks"], [123, "Sri", 100], [124, "Ganesh", 100], [125, "Keerthi", 99.5], [126, "Abishek", 99]]

#Appending the table
def apnd():
    print("Table data adder")
    roll = int(input("Enter the roll number of the students : "))
    name = input("Enter the name of the student : ")
    mark = float(input("Enter the marks of the student : "))
    lst = [roll, name, mark]
    tbl.append(lst)


#Viewing the row from a table
def view():
    roll = int(input("Enter the roll number : "))
    for i in tbl:
        if i[0] == roll:
            for j in tbl[0]:
                print(j, end = "\t\t")
            print()
            for k in i:
                print(k, end = '\t\t\t')
            print()
        """else:
            print("Enter the roll number which is present in the table")
            break"""


#To view the entire table
def full():
    for i in tbl[0]:
        print(i, end='\t\t')
    print()
    for j in range(1,len(tbl)):
        for k in tbl[j]:
            print(k, end='\t\t\t')
        print()
        

#The menu
print("Basic table management and database management in python",'\n')
sltr = "y"
while sltr in "yY":
    print()
    print("1 Add more rows to the table")
    print("2 View a row from the table")
    print("3 View the entire table")

    optn = int(input("Enter the number to execute : "))
    print()

    if optn == 1:
        apnd()
    elif optn == 2:
        view()
    elif optn == 3:
        full()
    else:
        print("Select the proper option" , '\n')

    print()

    sltr = input("To continue enter Y, to exit enter anything : ")
