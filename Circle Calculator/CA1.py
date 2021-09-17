#r_calculator calculates the remaining parameters of a circle given the radius(r) of thr ciecle
def r_calculator():
    #Ask the user to enter the radius of circle
    radius = float(input("Enter the radius of the circle in centimeters: ")) 
    print()
    print("The diameter of the circle is : {:.2f} cm".format(2*radius))
    print("The circumference of the circle is : {:.2f} cm".format(2*3.14*radius))
    print("The area of the circle is : {:.2f} cm".format(3.14*radius**2))

#c_calculator calculates the remaining parameters of a circle given the circumference(C) of the circle
def c_calculator():
    #Ask the user to enter the circumferencce
    circumference = float(input("Enter the circumference of the circle in centimeters : "))
    print()
    print("The radius of the circle is : {:.2f} cm".format(circumference/(2*3.14)))
    print("The diameter of the circle is : {:.2f} cm".format(circumference/3.14))
    print("The area of the circle is : {:.2f} cm".format(circumference**2/(4*3.14)))

#a_calculator calculates and out the remaining parameters of a circle given the area(a) of the circle
def a_calculator():
    #Ask the user to enter the area of circle
    area = float(input("Enter the area of the circle in centimeters : "))
    print()
    print("The radius of the circle is : {:.2f} cm".format((area/3.14)**0.5))
    print("The diameter of the circle is : {:.2f} cm".format(2*(area/3.14)**0.5))
    print("The circumference of the circle is : {:.2f} cm".format(2*3.14*(area/3.14)**0.5))
#while loop running untill user presses q
while(True):
    print()
    print("Enter 1, to calculate diameter (d), circumference (C) and area (A), given the radius (r) of a circle or q to quit")
    print("Enter 2, to calculate diameter (d), area (A) and radius (r), given circumference (C) of a circle or q to quit")
    print("Enter 3, to calculate diameter (d), radius (r) and circumference (C), given area (A) of a circle or q to quit")
    print()
    calculatorMenuInput = input() #asking user for input
    if calculatorMenuInput == "q" or calculatorMenuInput == "Q": #if input is equal to q, it will exit the programme
        exit()
    else:
        if calculatorMenuInput.isnumeric() == True: #checking if the input is of right format
            if int(calculatorMenuInput) == 1: # calling of defined functions according to input
                r_calculator()
            elif int(calculatorMenuInput) == 2:
                c_calculator()
            elif int(calculatorMenuInput) == 3:
                a_calculator()
            else:
                print()
                print("Enter the valid input from menu\n")
        else:
            print()
            print("Enter the valid input from menu\n")
            