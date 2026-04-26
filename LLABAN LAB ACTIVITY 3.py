def main():
    filename = "users.txt"

    try:
        # Ask user for input
        username = input("Enter username: ").strip()
        age_input = input("Enter age: ").strip()

        # Validate inputs
        if not username:
            raise ValueError("Username cannot be empty.")

        age = int(age_input)  # This can raise ValueError

        if age <= 0:
            raise ValueError("Age must be a positive number.")

        # Save to file
        with open(filename, "a") as file:
            file.write(f"{username} - {age}\n")

    except ValueError as ve:
        print(f"Input error: {ve}")

    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        # Display all saved users
        try:
            print("\nSaved Users:")
            with open(filename, "r") as file:
                data = file.read()
                if data:
                    print(data)
                else:
                    print("No users found.")
        except FileNotFoundError:
            print("No users file found yet.")

        print("System complete.")


# Run the program
main()