def temp_converter():
    print('\n--------Temperature Converter--------')
    value = float(input('Enter the temperature value:'))
    unit = input('Enter the temperature unit(C/F/K):').upper()

    if unit == 'C':
        print(f'{value}°C = {value * 9/5 + 32:.2f}°F')
        print(f'{value}°C = {value + 273.15:.2f}K')
    elif unit == 'F':
        print(f'{value}°F = {(value - 32) * 5/9:.2f}°C')
        print(f'{value}°F = {(value - 32) * 5/9 + 273.15:.2f}K')
    elif unit == 'K':
        print(f'{value}K = {value - 273.15:.2f}°C')
        print(f'{value}K = {(value - 273.15) * 9/5 + 32:.2f}°F')
    else:
        print('Invalid Unit')
    
def pressure_converter():
    print('\n---Pressure Converter---')
    value = float(input('Enter the pressure value:'))
    unit = input('Enter the pressure unit(Pa/bar/atm):').lower()

    if unit == 'pa':
        print(f"{value} Pa = {value/100000:.5f} bar = {value/101325:.5f} atm")
    elif unit == 'bar':
        print(f"{value} bar = {value*100000:.2f} Pa = {value/1.01325:.5f} atm")
    elif unit == 'atm':
        print(f"{value} atm = {value*101325:.2f} Pa = {value*1.01325:.5f} bar")
    else:
        print('Invalid Unit')
    
def velocity_converter():
    print('\n---Velocity Converter---')
    value = float(input('Enter the velocity:'))
    unit = input('Enter the unit (m/s, km/h, mph):').lower()

    if unit == 'm/s':
        print(f'{value}m/s = {value * 3.6:.2f}km/h')
        print(f'{value}m/s = {value * 2.23694:.2f}mph')
    elif unit == 'km/h':
        print(f'{value}km/h = {value / 3.6:.2f}m/s')
        print(f'{value}km/h = {value / 1.609:.2f}mph')
    elif unit == 'mph':
        print(f'{value}mph = {value / 2.23694:.2f}m/s')
        print(f'{value}mph = {value * 1.609:.2f}km/h')

def length_converter():
    print('\n---Length Converter---')
    value = float(input('Enter the length:'))
    unit = input('Enter the unit (m, cm, mm, ft):').lower()

    if unit == 'm':
        print(f'{value} m = {value * 100:.2f} cm')
        print(f'{value} m = {value * 1000:.2f} mm')
        print(f'{value} m = {value * 3.28084:.2f} ft')
    elif unit == 'cm':
        print(f'{value} cm = {value / 100:.4f} m')
        print(f'{value} cm = {value * 10:.2f} mm')
        print(f'{value} cm = {value / 30.48:.4f} ft')
    elif unit == 'mm':
        print(f'{value} mm = {value / 1000:.2f} m')
        print(f'{value} mm = {value / 10:.2f} cm')
        print(f'{value} mm = {value / 304.8:.4f} ft')
    elif unit == 'ft':
        print(f'{value} ft = {value * 0.3048:.4f} m')
        print(f'{value} ft = {value * 30.48:.2f} cm')
        print(f'{value} ft = {value * 304.8:.2f} mm')

def main():
    print("=== Engineering Unit Converter ===")
    while True:
        print("\nSelect category:")
        print("1. Temperature\n2. Pressure\n3. Velocity\n4. Length\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            temp_converter()
        elif choice == '2':
            pressure_converter()
        elif choice == '3':
            velocity_converter()
        elif choice == '4':
            length_converter()
        elif choice == '5':
            print('Exiting. Goodbye!')
            break
        else:
            print('Invalid Choice')

if __name__ == "__main__":
    main()