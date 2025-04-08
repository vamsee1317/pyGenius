users = {}

def registerUser(userName, password, cpassword):
    if userName in users:
        print("User already exists")
        return False
    else:
        users[userName] = {"password" : password, "cpassword" : cpassword}
        print("User registered successfully")
        return True
    
def loginUser(userName, password):
    if userName in users and users[userName]["password"] == password:
        print("Login successful")
        return True
    else:
        print("Invalid username or password")
        return False