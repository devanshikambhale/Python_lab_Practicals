#program to read temperatures in degree celsius.
temp=float(input("Enter temperature in degree Celsius: "))
if temp < -273.15:
    print("Invalid temperature: below absolute zero.")
elif temp == -273.15:
    print("Temperature is absolute zero.")
elif -273.15 < temp < 0:
    print("Temperature is below freezing")
elif temp == 0:
    print("Temperature is at freezing point.")
elif 0 < temp < 100:
    print("Temperature is in normal range.")
elif temp == 100:
    print("Temperature is at boiling point.")
elif temp > 100:
    print("Temperature is above boiling point.")