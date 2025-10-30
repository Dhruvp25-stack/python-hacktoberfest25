"""
Author: Dhruv Patni
Repository: Projects-and-Interview-Question-Hacktoberfest2025
File: email_validator.py

Description:
-------------
A simple Python script to validate email addresses using regular expressions.
This script checks if an entered email address follows the correct pattern.

Topics Covered:
- String handling
- Regular expressions (re)
- Basic input/output operations
"""

import re

def is_valid_email(email: str) -> bool:
    """
    Validates an email address using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def main():
    print("📧 Email Validator - Python Utility")
    print("----------------------------------")

    while True:
        email = input("\nEnter an email address to validate (or type 'exit' to quit): ").strip()
        if email.lower() == "exit":
            print("Exiting program. Goodbye! 👋")
            break

        if is_valid_email(email):
            print(f"✅ '{email}' is a valid email address.")
        else:
            print(f"❌ '{email}' is NOT a valid email address.")


if __name__ == "__main__":
    main()
