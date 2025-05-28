from temp_logger.converter import convert_temperature
from temp_logger.logger import log_conversion, read_log

def run_cli():
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
            log = read_log()
            if log:
                print("\n--- Conversion Log ---")
                for line in log:
                    print(line.strip())
            else:
                print("⚠️ No log file found yet.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")