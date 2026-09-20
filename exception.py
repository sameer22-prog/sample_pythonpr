a=int(input("Enter the password:"))
      
try:
    if a==2025:
        print("password is correct")
    else:
        print("check password")
except Exception:
    print("only in digit")
finally:
      print("thanks a lot you complete your work")
