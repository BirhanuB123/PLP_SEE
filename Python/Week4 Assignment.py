def process_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        new_filename = f"modified_{filename}"
        
        with open(new_filename, "w") as file:
            file.write(modified_content)
        
        print(f"✅ Success! Modified content saved to '{new_filename}'")
    
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"⚠️ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    user_file = input("Enter the filename you want to process: ")
    process_file(user_file)
