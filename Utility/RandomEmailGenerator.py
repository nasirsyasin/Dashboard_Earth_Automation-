import random
from Utility.common_cache import CommonCache


class RandomEmailGenerator:
    def __init__(self):
        self.base_email = "zubair.shahid@mavrictech.com"

    def generate_random_email(self):
        random_integer = random.randint(1, 99999)
        local_part, domain = self.base_email.split("@")
        random_email = f"{local_part}+{random_integer}@{domain}"
        CommonCache.set_email(random_email)
        return random_email

# rand_email = RandomEmailGenerator()
# config.email = rand_email.generate_random_email()


# def random_email_gen():
#     # random email generator
#     random_integer = random.randint(1, 99999)
#     # Original email address
#     email = "zubair.shahid@mavrictech.com"
#     # Split the email address into local part and domain
#     local_part, domain = email.split("@")
#     # Append the random integer to the local part
#     random_email = f"{local_part}+{random_integer}@{domain}"
#     return random_email
