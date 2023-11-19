import csv
import re

# Define a regular expression pattern for validating email addresses
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Function to validate an email address using regular expression
def is_valid_email(email):
    return re.match(email_pattern, email) is not None

# CSV file path
csv_file_path = "friends.csv"  # Replace with your CSV file path

try:
    # Open and read the CSV file
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
       
        print("List of Friends and Their Email IDs:")
       
        # Iterate through the rows in the CSV file
        for row in reader:
            if len(row) == 2:
                friend_name, friend_email = row
                if is_valid_email(friend_email):
                    print(f"Name: {friend_name}, Email: {friend_email} (Valid)")
                else:
                    print(f"Name: {friend_name}, Email: {friend_email} (Invalid)")
            else:
                print("Invalid row format:", row)
except FileNotFoundError:
    print("File not found:", csv_file_path)
except Exception as e:
    print("An error occurred:", str(e))
