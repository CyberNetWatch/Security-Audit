# password-checker.py  
import re  

def validate_password(password):  
    """Check if password meets complexity requirements and provide feedback."""  
    if len(password) < 8:  
        return "Password must be at least 8 characters long."  
    if not re.search(r"[A-Z]", password):  
        return "Password must contain at least one uppercase letter."  
    if not re.search(r"[0-9]", password):  
        return "Password must contain at least one digit."  
    if not re.search(r"[!@#$%^&*]", password):  
        return "Password must contain at least one special character (!@#$%^&*)."  
    return "Password is valid."  

def password_strength(password):  
    """Rate the password's strength."""  
    strength = 0  
    if len(password) >= 8:  
        strength += 1  
    if re.search(r"[A-Z]", password):  
        strength += 1  
    if re.search(r"[0-9]", password):  
        strength += 1  
    if re.search(r"[!@#$%^&*]", password):  
        strength += 1  
    if strength == 4:  
        return "Strong"  
    elif strength >= 2:  
        return "Medium"  
    else:  
        return "Weak"  

def save_valid_password(password):  
    """Save valid passwords to a file."""  
    with open("valid-passwords.txt", "a") as file:  
        file.write(password + "\n")  

# Example usage  
password = input("Enter a password to validate: ")  
result = validate_password(password)  
print(result)  

if result == "Password is valid.":  
    print(f"Password Strength: {password_strength(password)}")  
    save_valid_password(password)  
    print("Password saved to 'valid-passwords.txt'.")  
else:  
    print("Password not saved.")  