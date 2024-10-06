import random
userbalance = [0]
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def auth(email, password):
    if email == "test@gmail.com" or password == "1122":
        return True
    return False

def mail(num):
   random_num = random.randint(1000, 9999)
   msg = MIMEMultipart()
   msg['From'] = 'thedavitmanukyan@mail.ru'
   msg['To'] = 'martinhakobyan954@gmail.com'
   msg["Subject"] = 'Hastateq Dzer Mail hascen'
   
   msg.attach(MIMEText( f"Mek angamva ogtagorcman kod - {random_num}", 'plain'))
   server = smtplib.SMTP_SSL("smtp.mail.ru", 465)

   server.login("thedavitmanukyan@mail.ru", "y0xG0CGX5hntimArxVK8")

   server.sendmail("thedavitmanukyan@mail.ru", "martinhakobyan954@gmail.com", msg.as_string())
   if num == random_num:
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
    numb = int(input("Hastateq Email um uxarkvac kody"))
    if auth(email=email, password=password) and mail(num=numb):
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
