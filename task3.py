import re
import os

def extract_emails(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found. Please check the file path.")
        return

    # Read the input text file
    with open(input_file, "r") as f:
        content = f.read()

    # Regular expression pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails_found = re.findall(email_pattern, content)

    # Remove duplicates while preserving order
    unique_emails = list(dict.fromkeys(emails_found))

    if not unique_emails:
        print("No email addresses found in the file.")
        return

    # Save extracted emails to output file
    with open(output_file, "w") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} email address(es):")
    for email in unique_emails:
        print(" -", email)

    print(f"\nEmails saved to '{output_file}'")


if __name__ == "__main__":
    input_file = "sample_data.txt"     # change this to your input .txt file
    output_file = "extracted_emails.txt"
    extract_emails(input_file, output_file)