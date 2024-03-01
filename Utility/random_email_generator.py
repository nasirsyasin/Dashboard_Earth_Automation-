import random


def random_email_gen():
    # random email generator
    random_integer = random.randint(1, 99999)
    # Original email address
    email = "zubair.shahid@mavrictech.com"
    # Split the email address into local part and domain
    local_part, domain = email.split("@")
    # Append the random integer to the local part
    random_email = f"{local_part}+{random_integer}@{domain}"
    return random_email
