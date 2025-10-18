year=int(input("Enter the year :"))
if year%4!=0:
    print("Is not a leap year")
elif year%100!=0:
    print("Is a leap yaer")
elif year%400!=0:
    print("Is a Leap year")
else:
    print("Is not a leap yaer")

    
    