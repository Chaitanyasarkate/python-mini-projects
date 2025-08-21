

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def show_menu():
    print("\n=== UNIT CONVERTER ===")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Kilometers → Miles")
    print("4. Miles → Kilometers")
    print("5. Kilograms → Pounds")
    print("6. Pounds → Kilograms")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose conversion (1–7): ").strip()

        if choice == "1":
            c = float(input("Enter °C: "))
            print(f"{c}°C = {c_to_f(c):.2f}°F")
        elif choice == "2":
            f = float(input("Enter °F: "))
            print(f"{f}°F = {f_to_c(f):.2f}°C")
        elif choice == "3":
            km = float(input("Enter km: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        elif choice == "4":
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")
        elif choice == "5":
            kg = float(input("Enter kg: "))
            print(f"{kg} kg = {kg_to_pounds(kg):.2f} lbs")
        elif choice == "6":
            pounds = float(input("Enter lbs: "))
            print(f"{pounds} lbs = {pounds_to_kg(pounds):.2f} kg")
        elif choice == "7":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, please select 1–7.")

if __name__ == "__main__":
    main()
