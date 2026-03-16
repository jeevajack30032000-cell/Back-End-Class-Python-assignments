# 1.create user define exception in python

#A User Defined Exception is a custom error created by the programmer by inheriting the Exception class.

#1.

class InvalidMobileNumber(Exception):
    pass

try:
    MobileNumber =input("enter the mobilenumber: ")
    if len(MobileNumber) != 10 or not MobileNumber.isdigit():
        raise InvalidMobileNumber("number should be in 10digit only")
    print("valid number")

except InvalidMobileNumber as I:
    print("Invalidmobilenumber error:",I)


    
#2.

class PasswordLengthError(Exception):
    pass

try:
    password = input("enter the password")
    if len(password)<8:
        raise PasswordLengthError("password is too short")
    print("password accepted")

except PasswordLengthError as P:
    print("error:",P)
