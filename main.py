from functions import (
    register_user, authenticate_user, get_closing_prices, 
    analyze_closing_prices, save_to_csv, read_from_csv
)

def main():
    print("Welcome to the Stock Selection Tool")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if register_user(email, password):
                print("Registration successful!")
            else:
                print("Email already registered.")
        
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if authenticate_user(email, password):
                print("Login successful!")
                
                while True:
                    print("\n1. Analyze a stock")
                    print("2. View saved data")
                    print("3. Logout")
                    sub_choice = input("Choose an option: ")
                    
                    if sub_choice == "1":
                        ticker = input("Enter stock ticker (e.g., 1155.KL): ")
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        
                        try:
                            prices = get_closing_prices(ticker, start_date, end_date)
                            results = analyze_closing_prices(prices)
                            print("\nAnalysis Results:")
                            for key, value in results.items():
                                print(f"{key}: {value:.2f}")
                            save_to_csv(email, ticker, results, "user_data.csv")
                            print("Analysis saved successfully.")
                        except Exception as e:
                            print(f"Error: {e}")
                    
                    elif sub_choice == "2":
                        print("\nSaved Data:")
                        read_from_csv("user_data.csv")
                    
                    elif sub_choice == "3":
                        print("Logged out.")
                        break
                    
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid login credentials.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
