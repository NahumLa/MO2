#Author: Nahum Lamberson
#MO2Lab.py
#This app will accept students' names and gpa's and then tell the user if they are on the dean's list or honor roll. 

last_name = "initialize"
while(last_name != "zzz" or last_name != "ZZZ"):
    last_name = input("Enter the student's last name. Enter zzz if you are done entering students.")
    if(last_name == "zzz" or last_name == "ZZZ"):
        break
    first_name = input("Enter the student's first name.")
    student_gpa = float(input("What is the student's gpa?"))
    while(student_gpa < 0.0 and student_gpa > 4.0): #Making sure gpa is a valid one
        print("That is not a valid gpa!")
        student_gpa = input("What is the student's gpa?")
    if(student_gpa >= 3.25 and student_gpa < 3.5): #Testing entered gpa with conditionals
        print("The student has made the HONOR ROLL!")
    elif(student_gpa >= 3.5):
        print("The student has made the DEAN'S LIST!")
    else: #The student's gpa was lower than 3.25
        print("The student hasn't made the dean's list OR the honor roll.")
        
print("GOODBYE!") #Just a goodbye message for when they stop entering student's/using the app