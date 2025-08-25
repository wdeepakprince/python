logincredentials={"deepak":"dp","prince":"pr"}
authentication_status = "Failed"
print("\n")
print("User Authentication Service!")
print("\n")
username=input("Enter the username : ")
password=input("Enter the password : ")
print("\n")
print("Authenticating...")
print("\n")

def authentication():
    if(logincredentials [username]==password):
        return "Success"
    else:
        return "Failed"

if authentication()=="Success":
    print("Authentication is Successful!")
else:
    print("Authentication has Failed!")
print("\n")   
