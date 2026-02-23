import re 

number = input("Whats your mobile number?: ")

if re.search(r"^07\d{9}$", number):
    print("valid number")
else:
    print("Invalid")