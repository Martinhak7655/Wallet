userbalance = [0]

def auth(email, password):
    if email == "test@gmail.com" or password == "1122":
        return True
    return False

def getBallane():
    return userbalance[0]

def cashin(sum):
    if sum <= 100:
        return False
    userbalance[0] += sum
    return True

def cashout(sum):
    if sum <= 0 and sum > userbalance[0]:
        return False
    userbalance[0] -= sum
    return True

while True:
    email = input("Email: ")
    password = input("Password:  ")
    if auth(email=email, password=password):
        print("-" * 25)
        print("Register Succes")
        print("Check Balance: B")
        print("Cashin command: +")
        print("Cashout command: -")
        print("Exit: E")
        print("-" * 25)
        while True:
            command = input("Command: ")
            if command == "B":
                print(f"Balance: {getBallane()}, dram")
            elif command == "+":
                Sum = int(input("chashin: "))
                if cashin(sum=Sum):
                    print("Procces Succesed")
                else:
                    print("Ann error try again")
            elif command == "-":
                Sum = int(input("Cashout: "))
                if cashout(sum=Sum):
                    print("Procces Succesed")
                else:
                    print("An error try again")
            elif command == "E":
                print("Exit")
                break
    else:
        print("-" * 25)
        print("Invalid Email or Password")
        print("-" * 25)
