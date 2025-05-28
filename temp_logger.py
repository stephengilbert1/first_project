from datetime import datetime

def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def log_conversion(celsius, fahrenheit, kelvin):
    timestamp = datetime.now().isoformat()
    with open("temperature_log.csv", "a") as file:
        file.write(f"{timestamp},{celsius},{fahrenheit},{kelvin}\n")

def main():
    while True:
        print("\n--- Temperature Logger ---")
        print("1. Convert new temperature")
        print("2. View conversion log")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                f, k = convert_temperature(celsius)
                print(f"Fahrenheit: {f:.2f}")
                print(f"Kelvin: {k:.2f}")
                log_conversion(celsius, f, k)
                print("Logged conversion.")
            except ValueError:
                print("❗ Invalid input. Please enter a number.")
        elif choice == "2":
            try:
                with open("temperature_log.csv", "r") as file:
                    print("\n--- Conversion Log ---")
                    for line in file:
                        print(line.strip())
            except FileNotFoundError:
                print("⚠️ No log file found yet.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()