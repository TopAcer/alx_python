def validate_password(password):
    if len(password) < 8:
        return False
    
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if not (has_digit and has_uppercase and has_lowercase):
        return False
    if ' ' in password:
        return False

    return True