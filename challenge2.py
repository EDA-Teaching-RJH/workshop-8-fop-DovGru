import re 

student = input("Whats your ID?: ")

if re.search("^[A-Za-z]{4}\d{4}$", student):
    print("valid")
else:
    print("Invalid")