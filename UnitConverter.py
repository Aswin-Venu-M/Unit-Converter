title = " UNIT CONVERTER "
dot ="-"
equal = "="

'''
ctrl + /    :   Select and Comment
'''

print(f"{equal:=^50}")
print(f"{dot:-^50}")
print(f"{title:-^50}")
print(f"{dot:-^50}")
print("MODES : ")
print("\t1. Length (L)\n\t2. Weight (W)\n\t3. Temperature (T)")
print(f"{dot:-^50}")
userMode = input("Enter mode (L/W/T) : ")
print(f"{dot:-^50}")
# 1. Length (L)
if userMode =='L'or userMode == 'l':
    print(f"Conversions :")
    print("\t1. m to cm\n\t2. cm to m\n\t3. m to km\n\t4. km to m\n\t5. km to cm\n\t6. cm to km")
    print(f"{dot:-^50}")
    conversion = int(input("Select Conversion (1/2/3/4/5/6) : "))
    print()
    # 1. m to cm
    if conversion == 1:
        m = int(input("Enter value (m) : "))
        cm = m * 100
        print(f"{dot:-^50}")
        print(f"{m} m = {cm} cm")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 2. cm to m
    elif conversion == 2:
        cm = int(input("Enter value (cm) : "))
        m = cm / 100
        print(f"{dot:-^50}")
        print(f"{cm} cm = {m} m")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 3. m to km
    elif conversion == 3:
        m = int(input("Enter value (m) : "))
        km = m / 1000
        print(f"{dot:-^50}")
        print(f"{m} m = {km} km")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 4. km to m
    elif conversion == 4:
        km = int(input("Enter value (km) : "))
        m = km * 1000
        print(f"{dot:-^50}")
        print(f"{km} km = {m} m")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 5. km to cm
    elif conversion == 5:
        km = int(input("Enter value (km) : "))
        cm = km * 100000
        print(f"{dot:-^50}")
        print(f"{km} km = {cm} cm")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 6. cm to km
    elif conversion == 6:
        cm = int(input("Enter value (km) : "))
        km = cm / 100000
        print(f"{dot:-^50}")
        print(f"{cm} cm = {km} km")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    else:
        print("INVALID INPUT !!!")

# 2. Weight (W)
elif userMode=='W' or userMode == 'w':
    print(f"Conversions :")
    print("\t1. g to mg\n\t2. g to kg\n\t3. mg to g\n\t4. mg to kg\n\t5. kg to g\n\t6. kg to mg")
    print(f"{dot:-^50}")
    conversion = int(input("Select Conversion (1/2/3/4/5/6) : "))
    print()
    # 1. g to mg
    if conversion == 1:
        g = int(input("Enter value (g) : "))
        mg = g * 1000
        print(f"{dot:-^50}")
        print(f"{g} g = {mg} mg")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 2. g to kg
    elif conversion == 2:
        g = int(input("Enter value (g) : "))
        kg = g / 1000
        print(f"{dot:-^50}")
        print(f"{g} kg = {kg} kg")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 3. mg to g
    elif conversion == 3:
        mg = int(input("Enter value (mg) : "))
        g = mg / 1000
        print(f"{dot:-^50}")
        print(f"{mg} mg = {g} g")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # mg to  kg
    elif conversion == 4:
        mg = int(input("Enter value (mg) : "))
        kg = mg / 1000000
        print(f"{dot:-^50}")
        print(f"{mg} mg = {kg} kg")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # kg to g
    elif conversion == 5:
        kg = int(input("Enter value (kg) : "))
        g = kg * 1000
        print(f"{dot:-^50}")
        print(f"{kg} kg = {g} g")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # kg to mg
    elif conversion == 6:
        kg = int(input("Enter value (kg) : "))
        mg = kg * 1000000
        print(f"{dot:-^50}")
        print(f"{kg} kg = {mg} mg")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")

# 3. Temperature (T)
elif userMode=='T' or userMode == 't':
    print(f"Conversions :")
    print("\t1. Fahrenheit to Celsius\n\t2. Fahrenheit to Kelvin\n\t3. Celsius to Fahrenheit\n\t4. Celsius To Kelvin\n\t5. Kelvin to Fahrenheit\n\t6. Kelvin to Celsius")
    print(f"{dot:-^50}")
    conversion = int(input("Select Conversion (1/2/3/4/5/6) : "))
    print()
    # 1. Fahrenheit to Celsius
    if conversion == 1:
        f = int(input("Enter value (F) : "))
        c = (f-32) * (5/9)
        print(f"{dot:-^50}")
        print(f"{f} F = {c} C")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")

    # 2. Fahrenheit to Kelvin
    elif conversion == 2:
        f = int(input("Enter value (F) : "))
        k = ((f-32) * (5/9)) + 273.15
        print(f"{dot:-^50}")
        print(f"{f} F = {k} K")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 3. Celsius to Fahrenheit
    elif conversion == 3:
        c = int(input("Enter value (C) : "))
        f = (c * (9/5)) + 32
        print(f"{dot:-^50}")
        print(f"{c} C = {f} F")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 4. Celsius To Kelvin
    elif conversion == 4:
        c = int(input("Enter value (C) : "))
        k = c + 273.15
        print(f"{dot:-^50}")
        print(f"{c} C = {k} K")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 5. Kelvin to Fahrenheit
    elif conversion == 5:
        k = int(input("Enter value (K) : "))
        f = ((k - 273.15) * (9/5)) + 32
        print(f"{dot:-^50}")
        print(f"{k} K = {f} F")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")
    # 6. Kelvin to Celsius
    elif conversion == 6:
        k = int(input("Enter value (K) : "))
        c = k - 273.15
        print(f"{dot:-^50}")
        print(f"{k} K = {c} C")
        print(f"{dot:-^50}")
        print(f"{equal:=^50}")

else:
    print(f"INVALID MODE !!!")
    print(f"{dot:-^50}")
    print(f"{equal:=^50}")