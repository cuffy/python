#Se crea una función para validar el email
def is_valid_email(email):
    email = email.strip()
    valid_email = False
    if email != "":
        if len(email) > 2 and "@" in email:
            valid_email = True
    return valid_email


emails = ["hellopython", "hello@python.es", "   ", " @ "]
for email in emails:
    print(is_valid_email(email), end=" ")

