def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273
    return kelvin

def celcius_to_fahrenheit(celsius):
    fahrenheit_c = 9/5 * celsius + 32
    return fahrenheit_c

def kelvin_to_fahrenheit(kelvin):
    fahrenheit_k = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit_k

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return kelvin

def main():
    while True:
        temperature_kelvin = 200
        temperature_celsius = 200
        userinput = input("Masukkan satuan suhu (K/F/C), atau ketik 'x' untuk keluar:\n")
        
        if userinput.lower() == 'x':
            break

        if userinput.upper() == 'K':
            temperature_kelvin = float(input("Masukkan temperatur (Kelvin):\n"))
            kjadic = kelvin_to_celsius(temperature_kelvin) 
            print(f"{temperature_kelvin} Kelvin sama dengan {kjadic:.2f} Celsius ")

            kjadif = kelvin_to_fahrenheit(temperature_kelvin)
            print(f"{temperature_kelvin} Kelvin sama dengan {kjadif:.2f} Fahrenheit \n")

        elif userinput.upper() == 'C':
            temperature_celsius = float(input("Masukkan temperatur (celsius):\n"))
            cjadik = celsius_to_kelvin(temperature_celsius)
            print(f"{temperature_celsius} Celsius sama dengan {cjadik:.2f} Kelvin ")

            cjadif = celcius_to_fahrenheit(temperature_celsius)
            print(f"{temperature_celsius} Celsius sama dengan {cjadif:.2f} Fahrenheit \n")

        elif userinput.upper() == 'F':
            temperature_fahrenheit = float(input("Masukkan temperatur (fahrenheit):\n"))
            fjadic = fahrenheit_to_celsius(temperature_fahrenheit)
            print(f"{temperature_fahrenheit} Fahrenheit sama dengan {fjadic:.2f} Celsius ")

            fjadik = fahrenheit_to_kelvin(temperature_fahrenheit)
            print(f"{temperature_fahrenheit} Fahrenheit sama dengan {fjadik:.2f} Kelvin \n")

if __name__ == "__main__":
    main()
