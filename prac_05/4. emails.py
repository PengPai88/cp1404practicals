"""
Emails
Estimate: 30 minutes
Actual:   35 minutes
"""


def extract_name_from_email(email):
    local_part = email.split('@')[0]
    name_parts = local_part.split('.')
    name = ' '.join(name_parts).title()
    return name


email_to_name = {}

while True:
    email = input("Email: ").strip()
    if not email:
        break

    extracted_name = extract_name_from_email(email)
    confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

    if confirmation not in ('', 'y'):
        extracted_name = input("Name: ").strip()

    email_to_name[email] = extracted_name

print()
for email, name in email_to_name.items():
    print(f"{name} ({email})")