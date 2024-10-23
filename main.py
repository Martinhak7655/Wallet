import random
userbalance = [0]
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#avelacnel shat ogtaterer 

users = [

]

random_num = random.randint(1000, 9999)
def mail():
    msg = MIMEMultipart()
    msg['From'] ="thedavitmanukyan@mail.ru"
    msg['To'] = "martinhakobyan954@gmail.com"
    msg['Subject'] = "Hastateq dzer mail hascen"
    msg.attach(MIMEText( f"Mek angamva ogtagorcman kod - {random_num}", 'plain'))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

    server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")

    server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())

def front(hastatum=None, hastatum2=None):
    if hastatum == "grancvel":
        return True
    elif hastatum2 == "mutq gorcel":
        return True
    return False
random_id = random.randint(1000, 9999)
def grancum(email, password, verification):
    if len(password) >= 8:
        mail()
        users_grancum = {
            "id": random_id,
            "mail": email,
            "password": password,
            "balance": userbalance[0]
        }
        users.append(users_grancum)
        if verification == random_num:
            return True
    return False

def mutqgorcel(password2):
    for user in users:
        if password2 == user["password"]:
            return True
    return False

def getBallane():
    for user in users:
        return user["balance"]

def poxancum(sum, verify):
    print(random_id)
    if sum <= 0:
        return False
    for user in users:
        if verify == user["id"]:
            print(random_id)
            user["balance"] += sum
            msg = MIMEMultipart()
            msg['From'] ="thedavitmanukyan@mail.ru"
            msg['To'] = "martinhakobyan954@gmail.com"
            msg['Subject'] = "Dzer Hashivy"
            msg.attach(MIMEText(f"Dzer Hashvic poxancvele user {user["id"]} ogtatirocin"))
            server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

            server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")

            server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())

def cashin(sum):
    if sum <= 100:
        return False
    userbalance[0] += sum
    msg = MIMEMultipart()
    msg['From'] ="thedavitmanukyan@mail.ru"
    msg['To'] = "martinhakobyan954@gmail.com"
    msg['Subject'] = "Dzer Hashivy"
    msg.attach(MIMEText( f"Dzer Hasvin Avelacele - {sum}", 'plain'))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

    server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")

    server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())
    return True

def front2(harc2=None, harc3=None):
    if harc2 == "passwordy":
        return True
    elif harc3 == "maily":
        return True
    return False

def popoxum(parol, verify):
    print(random_id)
    if len(parol) < 8:
        return False
    for user in users:
        if verify == user["id"]:
            user["password"] = parol
            return True
    return False

def popoxum2(mail, verify):
    print(random_id)
    for user in users:
        if verify == user["id"]:
            user["mail"] = mail
            return True
    return False 

def cashout(sum):
    if sum <= 0 and sum > userbalance[0]:
        return False
    userbalance[0] -= sum
    msg = MIMEMultipart()
    msg['From'] ="thedavitmanukyan@mail.ru"
    msg['To'] = "martinhakobyan954@gmail.com"
    msg['Subject'] = "Dzer Hashivy"
    msg.attach(MIMEText( f"Dzer Hasvic hanvele - {sum}", 'plain'))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

    server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")

    server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())
    return True

while True:
    harc = input("Cankanumeq mutq gorcel te grancvel >>  ")
    if front(hastatum=harc):
        email = input("Email: ")
        password = input("Password:  ")
        numb = int(input("Hastateq emailum grvac kody >>>  "))
        if grancum(email=email, password=password, verification=numb):
            print("-" * 25)
            print("Register Succes")
            print("Check Balance: B")
            print("Cashin command: +")
            print("Cashout command: -")
            print("Poxancum: P")
            print("Popoxum: R")
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
                elif command == "P":
                    Sum = int(input("Poxancman gumary >>  "))
                    Verify = int(input("Greq ogtatiroj idn"))
                    if poxancum(sum=Sum, verify=Verify):
                        print("Procces Succesed")
                
                elif command == "R":
                    harcum = input("Cankanumeq popoxel passwordy te maily")
                    if front2(harc2=harcum):
                        Parol = input("Greq Dzer Popoxman Passwordy >>  ")
                        Verify = int(input("Greq idn"))
                        if popoxum(parol=Parol, verify=Verify):
                            print("Procces Succesed")
                        else:
                            print("An Error Try Again")
                    elif front2(harc3=harcum):
                        Maily = input("Greq Dzer Popoxman Maily >>  ")
                        Verify = int(input("Greq idn"))
                        if popoxum2(mail=Maily, verify=Verify):
                            print("Procces Succesed")
                        else:
                            print("An Error Try Again")
                elif command == "E":
                    print("Exit")
                    break
                else:
                    print("-" * 25)
                    print("Aydpisi command chka")
                    print("-" * 25)
        else:
            print("-" * 25)
            print("Invalid Email or Password")
            print("-" * 25)
    elif front(hastatum2=harc):
        password2 = input("password: ")
        if mutqgorcel(password2=password2):
            print("-" * 25)
            print("Register Succes")
            print("Check Balance: B")
            print("Cashin command: +")
            print("Cashout command: -")
            print("Poxancum: P")
            print("Popoxum: R")
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
                elif command == "P":
                    Sum = int(input("Poxancman gumary >>  "))
                    Verify = int(input("Greq ogtatiroj idn"))
                    if poxancum(sum=Sum, verify=Verify):
                        print("Procces Succesed")
                elif command == "R":
                    harcum = input("Cankanumeq popoxel passwordy te maily")
                    if front2(harc2=harcum):
                        Parol = input("Greq Dzer Popoxman Passwordy >>  ")
                        Verify = int(input("Greq idn"))
                        if popoxum(parol=Parol, verify=Verify):
                            print("Procces Succesed")
                        else:
                            print("An Error Try Again")
                    elif front2(harc3=harcum):
                        Maily = input("Greq Dzer Popoxman Maily >>  ")
                        Verify = int(input("Greq idn"))
                        if popoxum2(mail=Maily, verify=Verify):
                            print("Procces Succesed")
                        else:
                            print("An Error Try Again")
                elif command == "E":
                    print("Exit")
                    break
        else:
            print("An error try again")
    else:
        print("-" * 25)
        print("Aydpisi command chka")
        print("-" * 25)