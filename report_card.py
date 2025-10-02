# Student Report Card System
# Author: Jaskaran Singh , Krishna Arora , Garv Sharma , Saransh , Bhupinder Singh

for colorama import Fore , Style , init
# initialize colorama for colored text in console
init(autoreset=True)

# Function to calculate grade based on percentage
def calculate_grade(percentage):
  if percentage >= 90:
    return "A+"
  elif percentage >= 80:
    return "A"
  elif percentage >= 70:
    return "B"
  elif percentage >= 60:
    return "C"
  elif percentage >= 50:
    return "D"
  else:
    return "F (fail)"
    # Main Function to create report card
    def report_card():
      # Header
    print(Fore.CYAN + "="*45)
print(Fore.YELLOW + Style.BRIGHT + "     🎓 STUDENT REPORT CARD SYSTEM 🎓")
print(Fore.CYAN + "="*45 + "\n")
# Inputs
name = input(Fore.Green + "Enter Student Name :") # Student name input
roll = input(Fore.Green + "Enter Roll Number :") # Roll number input
num_subjects = int(input(Fore.Green + "Number of Subjects :")) # Number of subjects 
subjects = {}           # Dictionary to store subject names and marks
total = 0               # Variable to store total marks


print(Fore.MAGNETA + "\n---Enter Marks ---")
for i in range(num_subjects):
  sub = input(Fore.BLUE + f"Subjects {i+1}Name  : ") # Subjects name
  marks = float(input(Fore.BLUE + f"Marks in {sub} : ")) # Marks input
  subjects[sub] = marks
  total += marks    # Adding marks to total 

  # Calculate percentage and grade
  percentage = total / num_subjects
  grade = calculate_grade(percentage)

  # Report Card Display
  print("\n" + Fore.CYAN + "="*45)
  print(Fore.YELLOW + Style.BRIGHT + "STUDENT REPORT CARD")
  print(Fore.CYAN + "="*45)
  print(Fore.CYAN + f"Name   : {name}") 
  print(Fore.CYAN + f"RollNo   : {roll}")
  print(Fore.CYAN +"-"*45)
  print(Fore.MAGNETA + "{:<20} {:>10}.format("Subject", "marks"))
  print(Fore.CYAN + "-"*45)

  # Print each subject and marks (without color)
  for sub, marks in subjects.items():
  # Optional: color can be used if you want
    color = Fore.GREEN if marks >= 40 else Fore.RED
    print(color + "{:<20} {:>10}".format(sub,marks))

    # Print total, percentage and grade
     print(Fore.CYAN + "-"*45)
    print(Fore.YELLOW + f"Total Marks : {total}")
    print(Fore.YELLOW + f"percentage : {percentage:.2f}%")
    print(Fore.YELLOW + f"Grade :       {grade}%")
    print(Fore.GREEN + Style.BRIGHT + "      Best Wishes For Your Future ")
    print(Fore.CYAN + "="*45)

     # Run the program
    if__name__=="__main__":
    report_card()
    
    
  
  
  

    
    
