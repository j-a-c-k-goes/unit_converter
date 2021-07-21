"""
Unit Converter: Miles and Kilometers
"""
# ....................................................... Main Functions

def print_menu():
    print("1\tkilometers to miles")
    print("2\tmiles to kilometers")

    print("3\tkilograms to pounds")
    print("4\tpounds to kilograms")

    print("5\tfarenheit ot celsius")
    print("6\tcelsius to farenheit")

def km_to_miles():
    km =  float(input("enter distance in kilometers: "))
    miles = km / 1.609
    print("distance in miles\t{:.2f}".format(miles))

def miles_to_km():
    miles = float(input("enter distance in miles: "))
    km = miles * 1.609
    print("distance in kilometers\t{:.2f}".format(km))

def kilograms_to_pounds():
    kg = float(input("enter weight in kilograms: "))
    pounds = kg * 2.205
    print("weight in pounds\t{:.2f}lbs".format(pounds))
    
def pounds_to_kilograms():
    pounds =  float(input("enter weight in pounds: "))
    kg = pounds / 2.2046
    print("weight in kilograms\t{:.2f}kg".format(kg))

def farenheit_to_celsius():
    farenheit =  float(input("enter temperature in farenheit: "))
    celsius = (farenheit - 32) * (5/9)
    print("distance in miles\t{:.2f}C".format(celsius))

def celsius_to_farenheit():
    celsius = float(input("enter temperature in celsius: "))
    farenheit = celsius * (9/5) + 32
    print("temperature in farenhiet\t{:.2f}°".format(farenheit))
    
# ....................................................... Main Run
if __name__ == "__main__":
    while True:
        print_menu()
        print()
        choice = input("which conversion would you like to perform?: ")
        print()
        
        if choice == "1":
            km_to_miles()
        if choice == "2":
            miles_to_km()
        if choice == "3":
            kilograms_to_pounds()
        if choice == "4":
            pounds_to_kilograms()
        if choice == "5":
            farenheit_to_celsius()
        if choice == "6":
            celsius_to_farenheit()

        exit = input("do you want to exit? (y)es or (n)o?: ")

        if exit == "y":
            break
        else:
            print("no conversion selected")
            continue
