def get_studcount():
    print("\n")
    studentcount=int(input("Enter the number of students to be enrolled : "))
    return studentcount

def get_studname():
    print("\n")
    studname =input("Enter the Student Name : ")
    return studname

def get_studage():
    studage =int(input("Enter the Student Age : "))
    return studage

def get_studrollno():
    studrollno =input("Enter the Student Roll No : ")
    return studrollno

def get_subjmarks(i):
    subjmarks=float(input("Enter the Marks for " + i + " : "))
    return subjmarks
    
def get_subjgrade(i):
    if(i>90):
        return "A"
    elif(i>80):
        return "B"
    elif(i>70):
        return "C"
    else: return "D"

def get_average(i,j,k,l,m):
    subjavg=(1+j+k+l+m)/5
    return subjavg

def print_studdetails():
    print("\n")
    print("Student Details Provided")
    print("---------------------------------")
    print("Student Name : ",studname)
    print("Student Age : ",studage)
    print("Student Roll No : ",studrollno)
    print("\n")
    print("Subject Name | Marks | Grade")
    print("----------------------------------------")
    print("English | Marks : ", subjeng, " | Grade : ",gradeeng)
    print("Tamil   | Marks : ", subjtam, " | Grade : ",gradetam)
    print("Maths   | Marks : ", subjmat, " | Grade : ",grademat)
    print("Science | Marks : ", subjsci, " | Grade : ",gradesci)
    print("Social   | Marks : ", subjsoc, " | Grade : ",gradesoc)
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

    studname=get_studname()
    studage=get_studage()
    studrollno=get_studrollno()
    print("\n")
    
    subjeng=get_subjmarks("English")
    subjtam=get_subjmarks("Tamil")
    subjmat=get_subjmarks("Maths")
    subjsci=get_subjmarks("Science")
    subjsoc=get_subjmarks("Social")
    
    gradeeng=get_subjgrade(subjeng)
    gradetam=get_subjgrade(subjtam)
    grademat=get_subjgrade(subjmat)
    gradesci=get_subjgrade(subjsci)
    gradesoc=get_subjgrade(subjsoc)
    
    subjavg=get_average(subjeng,subjtam,subjmat,subjsci,subjsoc)
    avggrade=get_subjgrade(subjavg)
    
    print_studdetails()

# Program Ends
