import os
import datetime
admin = {"vijay": '90251'}
amount = {2000: 0, 500: 0, 200: 0, 100: 0}
users = [{'name': 'vijay', 'pass': 0000, 'balance': 100000, 'bank': "SBI", 'daily_limit': 10000, 'extra_charge': 10},
         {'name': 'mani', 'pass': 1000, 'balance': 80000, 'bank': "SBI", 'daily_limit': 10000, 'extra_charge': 10},
         {'name': 'abarna', 'pass': 2000, 'balance': 20000, 'bank': "IOB", 'daily_limit': 12000, 'extra_charge': 20}]
transcation = []
atm = {'bank': 'SBI', 'balance': 0}
atmdetail = None


def Ad():
    while(True):
        print("\tWelcome ADMIN")
        print('''    1.update
    2.show
    3.atm balance
    4.exit''')
        n = int(input("Enter your choice: "))
        if(n == 1):
            os.system('cls')
            print("\tUPDATE")
            for i in amount:
                x = int(input("enter no of"+str(i)+"--->"))
                amount[i] += x
                a = amount[i]*i
                atm['balance'] += a
                print("SUCCESSFULLY ADDED")
            input("press enter to continue.....")
            os.system('cls')
        elif(n == 2):
            os.system('cls')
            for i in amount:
                print(i, "-->", amount[i])
            input("press enter to continue.....")
            os.system('cls')
        elif(n == 3):
            atm['balance'] = 0
            for i in amount:
                a = amount[i]*i
                atm['balance'] += a
            print("Amount left in atm:", atm['balance'])

        elif(n == 4):
            break


def Cus(username, a, atm):
    os.system('cls')
    print("\n\n\t WELCOME", username)
    print('''1.Withdraw
    2.Show Balance
    3.transaction
    4.pin change
    5.direct deposite
    6.account transfer
    7.Exit''')
    while(True):
        n = int(input())
        if(n == 1):
            amt = int(input("ENTER THE AMOUNT:"))
            bal = a['balance']
            if(amt < atm['balance']):
                if(bal >= amt):
                    if(amt % 100 == 0):
                        if(amt < a['daily_limit']):
                            a['daily_limit'] -= amt
                            ref = 0
                            for i in amount:
                                no = int(input("Enter no of"+str(i)+":"))
                                if (no <= amount[i]):
                                    ref += i*no
                                    amount[i] -= no
                                    if (amt == ref):
                                        if(atm['bank'] == a['bank']):
                                            bal -= amt
                                            a['balance'] = bal
                                            val = amt, datetime.datetime.now()
                                            transcation.append([val])
                                            print("withdrawal success")
                                            break
                                        else:
                                            amount[i] -= no
                                            bal -= amt+a['extra_charge']
                                            a['balance'] = bal
                                            val = amt, datetime.datetime.now(
                                            ), a['extra_charge']
                                            transcation.append([val])
                                            print("withdrawal success")
                                            break
                                    elif(ref > amt):
                                        print(
                                            "amount is less than the entered amount\nplease try again correctly")
                                    elif(ref < amt):
                                        print(
                                            "Amount exceeded\nplease try again correctly")
                                else:
                                    print(str(i)+"not available")
                        else:
                            print("Daily limit already reached")
                    else:
                        print("enter correct amoun1t")
                else:
                    print("insufficient balance in account")
            else:
                print("insufficient balance in atm")
        elif(n == 2):
            bal = a['balance']
            print(bal)
        elif(n == 3):
            req = int(input("No of transaction required"))
            for i in range(0, req):
                print(transcation[i])
        elif(n == 4):
            b = int(input("enter your old pin: "))
            if(b == a['pass']):
                new = int(input("enter your new pin: "))
                a['pass'] = new
                print("pin changed successfully")
                break
            else:
                print("pin does not match")
        elif(n == 5):
            y=int(input("enter the amount to deposite: "))
            if(y%100==0):
                ref=0
                for i in amount:
                    no = int(input("Enter no of"+str(i)+":"))
                    ref += i*no
                    amount[i]+=no
                if(ref==y):
                    a['balance']+=y
                    print("amount deposited successfully")
                else:
                    print("deposite amount correctly")
            else:
                print("enter correct amount")
        elif(n==6):
            z=input("enter the benificiary name: ")
            ben=None
            for i in users:
                if(z == i['name']):
                    ben=i
                    v=int(input("enter the amount to transfer: "))
                    if(v<a['balance']):
                        a['balance']-=v
                        ben['balance']+=v
                        print("amount transfered successfully")
                        break
            else:
                print("enter a valid user")

        elif(n==7):
            break


admin_attempt = 3
user_attempt = 3
while(True):
    print("\n\n\tATM")
    print('''1.Admin
2.Customer
3.Exit''')
    n = int(input("enter your choice: "))
    os.system('cls')
    if(admin_attempt <= 0):
        break
    else:
        if(n == 1):
            username = input("Name:")
            Passwd = input("Password:")
            for x, y in admin.items():
                if(username == x and Passwd == y):
                    print("Succefully LoggedIn")
                    input("press enter to continue.....")
                    os.system('cls')
                    Ad()
                else:
                    print("Incorrect Password")
                    admin_attempt -= 1
                    print("Attempt Left:", admin_attempt)
                    input("press enter to continue.....")
                    os.system('cls')
        elif(n == 2):
            username = input("Name:")
            Pin = int(input("Pin:"))
            if(user_attempt > 0):
                for i in users:
                    if(username == i['name'] and Pin == i['pass']):
                        a = i
                        Cus(username, a, atm)
                        break
                else:
                    print("Incorrect Pass")
                    user_attempt -= 1
                    print("Attempt Left", user_attempt)
            else:
                exit()
        elif(n == 3):
            exit()
        else:
            print("Invalid Input")
