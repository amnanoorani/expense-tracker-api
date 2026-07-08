

def main_menu():
    
    
    print("UNIT CONVERTER")
    
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Exit")
    

def convert_length():
    
    print("Length Conversion ")
    print("Length: millimeter, centimeter, meter, kilometer, inch, foot, yard,mile")

    
    
    from_unit = input("Convert from : ").lower()
    to_unit = input("Convert to : ").lower()
    
    try:
        value = float(input("Enter value to convert: "))
    except:
        print("You entered invalid number!")
        return
    
    
    if from_unit == "millimeter":
        meters = value / 1000
    elif from_unit == "centimeter":
        meters = value / 100
    elif from_unit == "meter":
        meters = value
    elif from_unit == "kilometer":
        meters = value * 1000
    elif from_unit == "inch":
        meters = value * 0.0254
    elif from_unit == "foot":
        meters = value * 0.3048
    elif from_unit == "yard":
        meters = value * 0.9144
    elif from_unit == "mile":
        meters = value * 1609.34
    else:
        print("You entered invalid 'from' unit!")
        return
    
    
    if to_unit == "millimeter":
        result = meters * 1000
    elif to_unit == "centimeter":
        result = meters * 100
    elif to_unit == "meter":
        result = meters
    elif to_unit == "kilometer":
        result = meters / 1000
    elif to_unit == "inch":
        result = meters / 0.0254
    elif to_unit == "foot":
        result = meters / 0.3048
    elif to_unit == "yard":
        result = meters / 0.9144
    elif to_unit == "mile":
        result = meters / 1609.34
    else:
        print("YOU entered invalid 'to' unit!")
        return
    
    
    print(f"\n{value} {from_unit} = {result} {to_unit}")

def convert_weight():
    
    print("Weight Conversion ")
    print("Weight: milligram, gram, kilogram, ounce, pound")
    
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    
    try:
        value = float(input("Enter value to convert: "))
    except:
        print("Invalid number!")
        return
    
    
    if from_unit == "milligram":
        grams = value / 1000
    elif from_unit == "gram":
        grams = value
    elif from_unit == "kilogram":
        grams = value * 1000
    elif from_unit == "ounce":
        grams = value * 28.3495
    elif from_unit == "pound":
        grams = value * 453.592
    else:
        print("YOU entered invalid 'from' unit!")
        return
    
    
    if to_unit == "milligram":
        result = grams * 1000
    elif to_unit == "gram":
        result = grams
    elif to_unit == "kilogram":
        result = grams / 1000
    elif to_unit == "ounce":
        result = grams / 28.3495
    elif to_unit == "pound":
        result = grams / 453.592
    else:
        print("YOU entered invalid 'to' unit!")
        return
    
    print(f"\n{value} {from_unit} = {result} {to_unit}")

def convert_temperature():
    
    print("Temperature Conversion ")
    print("Temperature: Celsius, Fahrenheit, Kelvin")
    
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    
    
    try:
        value = float(input("Enter value to convert: "))
    except:
        print("You entered invalid number!")
        return
    

    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        print("You entered invalid 'from' unit!")
        return
    
    
    if to_unit == "celsius":
        result = celsius
    elif to_unit == "fahrenheit":
        result = (celsius * 9 / 5) + 32
    elif to_unit == "kelvin":
        result = celsius + 273.15
    else:
        print("you entered invalid 'to' unit!")
        return
    
    print(f"\n{value} {from_unit} = {result} {to_unit}")

def main():
    
    while True:
        main_menu()
        choice = input("Enter your choice from 1 to 4 ")
        
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        
        input("Press Enter to continue...")


main()
