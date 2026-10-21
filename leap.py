yr = int(input("Enter year :"))
if yr % 4 == 0 or yr % 100 == 0:
    print("Leap year")
else:
    print("Non leap year")