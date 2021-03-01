from bmi import bmi

from retirement import savings_per_year, num_years_till_goal, age_when_goal_met

def main():
    Exit=False
    option=0
    while(Exit==False):
        while(option<=0 or option>=4):
            try:
                option=int(input("\nWhich option would you like to select 1-BMI or 2-Retirement or 3-Exit: "))
                if(option<=0 or option>=4):
                    print("\n Error occured please a make sure to only enter 1, 2, or 3\n")
            except:
                print("\n Error occured please a make sure to only enter 1, 2, or 3\n")
        if(option==3):
            print("\n Ending Program")
            Exit=True

        elif(option==2):
            
            age=0
            salary=0
            per_saved=0
            goal=0
            while(age<=0):
                try:
                    age=int(input("Please enter your age: "))
                    if(age<=0):
                        print("\n Error occured please enter a positive non zero number for age\n")
                except:
                    print("\n Error occured please make sure to enter a positive non zero number for age\n")

            while(salary<=0):
                try:
                    salary=int(input("Please enter your salary: "))
                    if(salary<=0):
                        print("\n Error occured please enter a positive non zero number for your salary\n")
                except:
                    print("\n Error occured please enter a positive non zero number for your salary\n")

            while(per_saved<=0 or per_saved>100):
                try:
                    print("\nValues can range from 0 to 100")
                    per_saved=float(input("Please enter the integer value for the percent you save for retirement: "))
                    if(per_saved<0):
                        print("\n Error occured percantage saved must be bigger than zero\n")
                    elif(per_saved>100):
                        print("\n Error occured percanage must be smaller than 100\n")  
                except:
                    print("\n Error occured please enter a positive number for your percent saved\n")
            per_saved/=100

            while(goal<=0):
                try:
                    goal=int(input("Please enter your goal: "))
                    if(goal<=0):
                        print("\n Error occured please enter a positive non zero number for your goal\n")
                except:
                    print("\n Error occured please make sure to enter a positive non zero number for your goal\n")

            ev=age_when_goal_met(age,salary,per_saved,goal)
            if(ev[1]==True):
                print("\nYou will be "+str(ev[0])+" When you reach $"+str(goal)+" for retirement.")

            else:
                print("\nYou can not achieve $"+str(goal)+" for retirement because you will be "+str(ev[0])+".")

            option=0

        else:
            weight=0
            heightft=0
            heightin=-1

            while(weight<=0):
                try:
                    weight=float(input("\nPlease enter your weight in pounds: "))
                    if(weight<=0):
                        print("\nError occured please enter a postive non zero number for your weight\n")
                except:
                    print("\nError occured please enter a postive non zero number for your weight\n")

            while(heightft<=0):
                try:
                    heightft=int(input("Please enter your height to the closest foot, inches will be entered later: "))
                    if(heightft<=0):
                        print("\nError occured please enter a postive non zero number for your height in feet\n")
                    if(heightft>11):
                        print("\nError occured please enter a value below 12\n")
                except:
                    print("\nError occured please enter a postive non zero number for your height in feet\n")

            while(heightin<0 or heightin>11):
                try:
                    heightin=int(input("Please enter your height to the closest inch: "))
                    if(heightin<0):
                        print("\nError occured please enter a postive number for your height in inches")
                    if(heightin>11):
                        print("\nError occured please enter a value below 12\n")
                except:
                    print("\nError occured please enter a postive number for your height in inches\n")
            bmi_eval=bmi(weight,heightft,heightin)

            print("Your bmi is: "+str(bmi_eval[0])+" which means you are "+ str(bmi_eval[1])+".")
            option=0
            
main()
