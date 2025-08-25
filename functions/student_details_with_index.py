studdetails=[["",0,""]]
studmarklist=[[0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
studgradelist=[["","","","","","",""]]

def get_studcount():
    print("\n")
    studentcount=int(input("Enter the number of students to be enrolled : "))
    return studentcount

def get_studname(i):
    print("\n")
    studdetails [i][0] =input("Enter the Student Name : ")

def get_studage(i):
    studdetails [i][1] =int(input("Enter the Student Age : "))

def get_studrollno(i):
    studdetails [i][2] =input("Enter the Student Roll No : ")

def get_subjmarks(i):
    print("\n")
    studmarklist [i][0]=float(input("Enter the Marks for English : "))
    studmarklist [i][1]=float(input("Enter the Marks for Tamil : "))
    studmarklist [i][2]=float(input("Enter the Marks for Maths : "))
    studmarklist [i][3]=float(input("Enter the Marks for Science : "))
    studmarklist [i][4]=float(input("Enter the Marks for Social : "))
    for j in range(0,5):
        get_subjgrade(i,j)


def get_subjgrade(i,j):
    if(studmarklist [i][j]>90):
        studgradelist [i][j] = "A"
    elif(studmarklist [i][j]>80):
        studgradelist [i][j] = "B"
    elif(studmarklist [i][j]>70):
        studgradelist [i][j] = "C"
    else: studgradelist [i][j] = "D"

def get_average(i):
    for j in range(0,5):
        studmarklist [i][5]+= studmarklist [i][j]
    studmarklist [i][6] = studmarklist [i][5] /5
    get_subjgrade(i,6)
    

def print_studdetails(i):
    print("\n")
    print("Student Details Provided")
    print("---------------------------------")
    print("Student Name : ",studdetails[i][0])
    print("Student Age : ",studdetails[i][1])
    print("Student Roll No : ",studdetails[i][2])
    print("\n")
    print("Subject Name | Marks | Grade")
    print("----------------------------------------")
    print("English | Marks : ", studmarklist [i][0], " | Grade : ",studgradelist [i][0])
    print("Tamil   | Marks : ", studmarklist [i][1], " | Grade : ",studgradelist [i][1])
    print("Maths   | Marks : ", studmarklist [i][2], " | Grade : ",studgradelist [i][2])
    print("Science | Marks : ", studmarklist [i][3], " | Grade : ",studgradelist [i][3])
    print("Social   | Marks : ", studmarklist [i][4], " | Grade : ",studgradelist [i][4])
    print("\n")
    
    
def print_avg(i):
    print("Total Marks : ",studmarklist [i][5])
    print("Average Marks : ", studmarklist [i][6])
    print("Cumulative Grade : ",studgradelist [i][6])    

# Program Starts

studentcount = get_studcount()
for i in range(0, studentcount):
    print("\n")
    print("Student #",i+1)
    get_studname(i)
    get_studage(i)
    get_studrollno(i)
    get_subjmarks(i)
    get_average(i)
    print_studdetails(i)
    print_avg(i)

# Program Ends
