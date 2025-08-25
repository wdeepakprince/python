import modules.studcount
import modules.studname
import modules.studage
import modules.studrollno
import modules.subjmarks
import modules.subjgrade
import modules.subjaverage

def print_studdetails():
    print("\n")
    print("Student Details Provided")
    print("------------------------")
    print("Student Name    : ",studname)
    print("Student Age     : ",studage)
    print("Student Roll No : ",studrollno)
    print("\n")
    print("Subject Name | Marks | Grade")
    print("-----------------------------")
    print("English | Marks : ", subjeng, " | Grade : ",gradeeng)
    print("Tamil   | Marks : ", subjtam, " | Grade : ",gradetam)
    print("Maths   | Marks : ", subjmat, " | Grade : ",grademat)
    print("Science | Marks : ", subjsci, " | Grade : ",gradesci)
    print("Social  | Marks : ", subjsoc, " | Grade : ",gradesoc)
    print("\n")

def print_avg():
    subjtotal=subjeng+subjtam+subjmat+subjsci+subjsoc
    print("Total Marks      : ",subjtotal)
    print("Average Marks    : ", subjtotal/5)
    print("Cumulative Grade : ",modules.subjgrade.get_subjgrade(subjtotal/5))  



# Program Starts

studentcount = modules.studcount.get_studcount()
for i in range(0, studentcount):
    print("\n")
    print("Student #",i+1)

    studname=modules.studname.get_studname()
    studage=modules.studage.get_studage()
    studrollno=modules.studrollno.get_studrollno()
    print("\n")
    
    subjeng=modules.subjmarks.get_subjmarks("English")
    subjtam=modules.subjmarks.get_subjmarks("Tamil")
    subjmat=modules.subjmarks.get_subjmarks("Maths")
    subjsci=modules.subjmarks.get_subjmarks("Science")
    subjsoc=modules.subjmarks.get_subjmarks("Social")
    
    gradeeng=modules.subjgrade.get_subjgrade(subjeng)
    gradetam=modules.subjgrade.get_subjgrade(subjtam)
    grademat=modules.subjgrade.get_subjgrade(subjmat)
    gradesci=modules.subjgrade.get_subjgrade(subjsci)
    gradesoc=modules.subjgrade.get_subjgrade(subjsoc)
    
    subjavg=modules.subjaverage.get_average(subjeng,subjtam,subjmat,subjsci,subjsoc)
    avggrade=modules.subjgrade.get_subjgrade(subjavg)
    
    print_studdetails()
    print_avg()

# Program Ends
