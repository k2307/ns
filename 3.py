import re
def check_password_strength(password):
    strength = 0
    remarks = ""
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long\n"
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter\n"

    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter\n"

   
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "Add at least one number\n"

  
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "Add at least one special character\n"

   
    if strength == 5:
        return "Strong Password 💪"
    elif strength >= 3:
        return "Medium Password ⚠️\n" + remarks
    else:
        return "Weak Password ❌\n" + remarks

password = input("Enter your password: ")
result = check_password_strength(password)

print("\nPassword Strength:", result)