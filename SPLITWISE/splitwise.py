import datetime
import time
import os
users = [{'name': 'user1', 'mail': 'user1@gmail.com', 'passwd': '1234', 'user_wallet': 7000},
         {'name': 'vijay', 'mail': 'vijay@gmail.com',
             'passwd': '1234', 'user_wallet': 5000},
         {'name': 'vishal', 'mail': 'vishal@gmail.com', 'passwd': '1234', 'user_wallet': 6000}]
members = [{'grp_name': 'bachelor', 'member': 'vijay', 'member_wallet': 5000},
           {'grp_name': 'bachelor', 'member': 'vishal', 'member_wallet': 6000},
           {'grp_name': 'bachelor', 'member': 'user1', 'member_wallet': 7000}]
notification = []
non_grpnotification = []
status = []
non_grpstatus = []
non_grpsts = []
history = []
non_grpmem = [{'exp_name': 'food', 'paid_by': 'user1', 'expense_creater': 'user1', 'expense_amount': 1000, 'mems': 'vijay', 'mems_wal': 5000, 'share': 100, 'status': 'PENDING', 'date': None},
              {'exp_name': 'food', 'paid_by': 'user1', 'expense_creater': 'user1', 'expense_amount': 1000, 'mems': 'vishal',
                  'mems_wal': 6000, 'share': 200, 'status': 'PENDING', 'date': None},
              {'exp_name': 'food', 'paid_by': 'user1', 'expense_creater': 'user1', 'expense_amount': 1000, 'mems': 'user1', 'mems_wal': 7000, 'share': 700, 'status': 'PENDING', 'date': None}]
non_group = [{'name': 'user1', 'exp_name': 'food'}]
group = [{'name': 'user1', 'grp_name': 'bachelor', 'member': members}]
title = "WELCOME TO SPLITWISE.....\nA NEW METHOD TO SHARE YOUR EXPENSE\n"
for i in title:
    time.sleep(0.05)
    print(i, end='')
input('PRESS ENTER TO CONTINUE......')
os.system('cls')


def bal(username):
    for i in users:
        if(i['name'] == username):
            print("WALLET BALANCE: {}".format(i['user_wallet']))
    input("PRESS ENTER TO CONTINUE.....")
    os.system('cls')


def his(username):
    if(len(history) > 0):
        print("1.GROUP\n2.NON - GROUP\n3.EXIT\n")
        k=int(input("ENTER YOUR CHOICE: "))
        if(k==1):
            for i in history:
                if(i['mem_name'] == username):
                    print("GROUP NAME: {}\nEXPENSE CREATOR: {}\nEXPENSE NAME: {}\nEXPENSE AMOUNT: {}\nYOUR SHARE: {}\nSTATUS: {}\nDATE: {}\n".format
                        (i['grp_name'], i['expense_creater'], i['expense_name'], i['expense_amount'], i['expense_share'], i['status'], i['date']))
                    print()
            input("PRESS ENTER TO CONTINUE.....")
        elif(k==2):
            for i in history:
                if(i['mems'] or i['mem_name'] == username):
                    print("EXPENSE PAID BY: {}\nEXPENSE CREATOR: {}\nMEMBER NAME: {}\nEXPENSE NAME: {}\nEXPENSE AMOUNT: {}\nYOUR SHARE: {}\nSTATUS: {}\nDATE: {}\n".format
                        (i['paid_by'], i['expense_creater'], i['mems'], i['exp_name'], i['expense_amount'], i['share'], i['status'], i['date']))
            input("PRESS ENTER TO CONTINUE.....")
        elif(k==3):
            input("PRESS ENTER TO CONTINUE.....")
        os.system('cls')
    else:
        print("NO RECORDS\n")
        input("PRESS ENTER TO CONTNUE.....")
        os.system('cls')


def settleup(username):
    print("1.GROUP\n2.NON - GROUP\n3.EXIT\n")
    y = int(input("ENTER YOUR CHOICE: "))
    print()
    if(y == 1):
        os.system('cls')
        for i in notification:
            if(i['mem_name'] == username and i['status'] == 'PENDING'):
                print("GROUP NAME: {}\nEXPENSE CREATOR: {}\nEXPENSE NAME: {}\nEXPENSE AMOUNT: {}\nYOUR SHARE: {}\nSTATUS: {}\nDATE: {}\n".format
                      (i['grp_name'], i['expense_creater'], i['expense_name'], i['expense_amount'], i['expense_share'], i['status'], i['date']))
                print()
                print("1.SETTLE UP\n2.EXIT")
                n = int(input("ENTER YOUR CHOICE: "))
                if(n == 1):
                    amt = int(input("ENTER THE AMOUNT: "))
                    for j in users:
                        if(j['name'] == username):
                            j['user_wallet'] -= i['expense_share']
                    for k in members:
                        if(k['member'] == username):
                            k['member_wallet'] -= i['expense_share']
                    i['status'] = 'PAID'
                    i['date'] = datetime.date.today()
                    for m in status:
                        if(m['mem_name'] == username):
                            m['status'] = 'PAID'
                            m['date'] = datetime.date.today()
                    history.append(i)
                    print("SETTLED UP SUCCESSFULLY")
                elif(n == 2):
                    break
                input("PRESS ENTER TO CONTINUE.....")
                break
            #{'exp_name': 'food', 'paid_by': 'user1', 'expense_creater': 'user1', 'expense_amount': 1000, 'mems': 'vishal','mems_wal': 6000, 'share': 200, 'status': 'PENDING', 'date': None}
    elif(y == 2):
        os.system('cls')
        for i in non_grpnotification:
            if(i['mems'] == username and i['status'] == 'PENDING'):
                print("EXPENSE PAID BY: {}\nEXPENSE CREATOR: {}\nMEMBER NAME: {}\nEXPENSE NAME: {}\nEXPENSE AMOUNT: {}\nYOUR SHARE: {}\nSTATUS: {}\nDATE: {}\n".format
                      (i['paid_by'], i['expense_creater'], i['mems'], i['exp_name'], i['expense_amount'], i['share'], i['status'], i['date']))
                print()
                print("1.SETTLE UP\n2.EXIT")
                n = int(input("ENTER YOUR CHOICE: "))
                if(n == 1):
                    amt = int(input("ENTER THE AMOUNT: "))
                    for j in users:
                        if(j['name'] == username):
                            j['user_wallet'] -= i['share']
                    i['status'] = 'PAID'
                    i['date'] = datetime.date.today()
                    for m in non_grpmem:
                        if(m['mems'] == username):
                            m['status'] = 'PAID'
                            m['date'] = datetime.date.today()
                    history.append(i)
                    print("SETTLED UP SUCCESSFULLY")
                elif(n == 2):
                    break
                input("PRESS ENTER TO CONTINUE.....")
                break


def userfun(username):
    while(True):
        print("1.GROUP\n2.EXPENSE\n3.FRIENDS\n4.SETTLE UP\n5.WALLET BALANCE\n6.PAYMENT HISTORY\n7.EXIT\n")
        b = int(input("ENTER YOUR CHOICE: "))
        if(b == 1):
            os.system('cls')
            print("**********GROUP**********\n")
            print("1.EXISITING GROUP\n2.NEW GROUP\n3.EXIT\n")
            f = int(input("ENTER YOUR CHOICE: "))
            if(f == 1):
                os.system('cls')
                print("**********EXISTING GROUP*********\n")
                grpname = input("ENTER THE GROUP NAME: ")
                for i in group:
                    if(i['grp_name'] == grpname):
                        os.system('cls')
                        print("**********", i['grp_name'], "**********\n")
                        print("1.SHOW MEMBERS\n2.ADD MEMBER\n")
                        a = int(input("ENTER YOUR CHOICE: "))
                        if(a == 1):
                            os.system('cls')
                            print("**********MEMBERS**********\n")
                            for j in members:
                                if(j['grp_name'] == grpname):
                                    print("NAME: {}\nWALLET: {}\n".format(
                                        j['member'], j['member_wallet']))
                            input("PRESS ENTER TO CONTINUE.....")
                            os.system('cls')
                        elif(a == 2):
                            os.system('cls')
                            print("**********ADD MEMBERS**********\n")
                            q = int(input("ENTER THE NUMBER OF MEMBER TO ADD: "))
                            print()
                            for _ in range(q):
                                name = input("ENTER THE NEW MEMBER NAME: ")
                                print()
                                wal = input("ENTER THE WALLET AMOUNT: ")
                                print()
                                newmem = {}
                                newmem['grp_name'] = grpname
                                newmem['name'] = name
                                newmem['member_wallet'] = wal
                                members.append()
                            print("MEMBER ADDED SUCCESSFULLY.....\n")
                            input("PRESS ENTER TO CONTINUE.....")
                            break

            elif(f == 2):
                newgrp = {}
                os.system('cls')
                print("**********NEW GROUP*********\n")
                creatername = username
                newname = input("ENTER THE NEW GROUP NAME: ")
                n = int(input("ENTER THE NUMBER OF MEMBERS TO BE ADDED: "))
                for i in range(n):
                    newmember = {}
                    newmembername = input("ENTER THE NEW MEMBER NAME: ")
                    newmemberwallet = int(
                        input("ENTER THE NEW MEMBER WALLET: "))
                    newmember['grp_name'] = newname
                    newmember['member'] = newmembername
                    newmember['member_wallet'] = newmemberwallet
                    members.append(newmember)
                newgrp['name'] = creatername
                newgrp['grp_name'] = newname
                newgrp['member'] = members
                group.append(newgrp)
                print("NEW GROUP CREATED SUCCESSFULLY")
                input("PRESS ENTER TO CONTINUE.....")
                os.system('cls')
        elif(b == 2):
            os.system('cls')
            print("**********EXPENSE*********\n")
            print("1.GROUP EXPENSE\n2.NON - GROUP EXPENSE\n3.EXIT\n")
            expencetype = int(input("ENTER YOUR CHOICE: "))
            if(expencetype == 1):
                os.system('cls')
                print("**********GROUP EXPENSE*********\n")
                print("1.EXISTING EXPENSE\n2.NEW EXPENSE\n3.EXIT\n")
                x = int(input("ENTER YOUR CHOICE: "))
                if(x == 1):
                    os.system('cls')
                    print("**********EXISTING EXPENSE*********\n")
                    print("1.VIEW STATUS\n2.EXIT\n")
                    y = int(input("ENTER YOUR CHOICE: "))
                    if(y == 1):
                        for i in status:
                            print("GROUP NAME: {}\nEXPENSE CREATOR: {}\nMEMBER NAME: {}\nEXPENSE NAME: {}\nEXPENSE AMOUNT: {}\nYOUR SHARE: {}\nSTATUS: {}\nDATE: {}\n".format
                                  (i['grp_name'], i['expense_creater'], i['mem_name'], i['expense_name'], i['expense_amount'], i['expense_share'], i['status'], i['date']))
                    elif(y == 2):
                        break
                elif(x == 2):
                    os.system('cls')
                    print("**********NEW EXPENSE*********\n")
                    grp_ = input("ENTER THE GROUP NAME: ")
                    print()
                    for i in group:
                        if(grp_ == i['grp_name']):
                            expname = input("ENTER THE EXPENSE NAME: ")
                            print()
                            expamount = int(
                                input("ENTER THE EXPENSE AMOUNT: "))
                            print()
                            share = expamount//len(members)
                            for i in members:
                                d = datetime.date.today()
                                sta = {}
                                noti = {}
                                noti['expense_creater'] = username
                                noti['grp_name'] = grp_
                                noti['mem_name'] = i['member']
                                noti['expense_name'] = expname
                                noti['expense_amount'] = expamount
                                noti['expense_share'] = share
                                noti['status'] = 'PENDING'
                                noti['date'] = None
                                sta = {}
                                sta['expense_creater'] = username
                                sta['grp_name'] = grp_
                                sta['mem_name'] = i['member']
                                sta['expense_name'] = expname
                                sta['expense_amount'] = expamount
                                sta['expense_share'] = share
                                sta['status'] = 'PENDING'
                                sta['date'] = None
                                notification.append(noti)
                                status.append(sta)
                            print("EXPENSE ADDED SUCCESSFULLY\n")
                            input("PRESS ENTER TO CONTINUE....")
                            break
                        # non_grpmem=[{'exp_name':'food','mems':users}]
                        # non_group=[{'name':'user1','exp_name':'food','mem':non_grpmem}]
            elif(expencetype == 2):
                os.system('cls')
                print("**********NON - GROUP EXPENSE*********\n")
                print("1.EXISTING EXPENSE\n2.NEW EXPENSE\n3.EXIT\n")
                ch = int(input("ENTER YOUR CHOICE: "))
                if(ch == 1):
                    os.system('cls')
                    print("**********EXISTING EXPENSE*********\n")
                    na = input("ENTER THE EXPENSE NAME: ")
                    for i in non_group:
                        if(i['name'] == username and i['exp_name'] == na):
                            print("1.VIEW STATUS\n2.EXIT\n")
                            k = int(input("ENTER YOUR CHOICE: "))
                            if(k == 1):
                                os.system('cls')
                                print("**********STATUS*********\n")
                                for j in non_grpmem:
                                    print("EXPENSE PAID BY: {}\nEXPENSE CREATOR: {}\nMEMBER NAME: {}\nEXPENSE NAME: {}\nEXPENSE AMOUNT: {}\nYOUR SHARE: {}\nSTATUS: {}\nDATE: {}\n".format
                                          (j['paid_by'], j['expense_creater'], j['mems'], j['exp_name'], j['expense_amount'], j['share'], j['status'], j['date']))
                                input("PRESS ENTER TO CONTINUE.....")
                                break
                            elif(k == 2):
                                input('PRESS ENTER TO CONTINUE.....')
                                break
                elif(ch == 2):
                    os.system('cls')
                    print("**********NEW EXPENSE*********\n")
                    expname = input("ENTER THE EXPENSE NAME: ")
                    print()
                    expamount = int(
                        input("ENTER THE EXPENSE AMOUNT: "))
                    x = int(input("ENTER THE NUMBER OF MEMBERS: "))
                    paidby = input("ENTER NAME OF PERSON WHOM PAID: ")
                    print("1.EQUALLY\n2.UNEQUALLY\n")
                    typ = int(input("ENTER THE TYPE OF SHARING: "))
                    if(typ == 1):
                        share = expamount//x
                        for i in range(x):
                            name = input("ENTER THE MEM NAME: ")
                            ne = {}
                            ng = {}
                            ne['exp_name'] = expname
                            ng['name'] = username
                            ng['exp_name'] = expname
                            ne['paid_by'] = paidby
                            ne['expense_creater'] = username
                            ne['expense_amount'] = expamount
                            ne['mems'] = name
                            ne['share'] = share
                            ne['status'] = 'PENDING'
                            ne['date'] = None
                            for j in users:
                                if(j['name'] == name):
                                    ne['mems_wal'] = j['user_wallet']
                                    break
                            non_grpmem.append(ne)
                            non_group.append(ng)
                        print("EXPENSE ADDED SUCCESSFULLY\n")
                        input("PRESS ENTER TO CONTINUE....")
                        break
                    # non_grpmem=[{'exp_name':'food','mems':'vijay','mems_wal':5000,'share':100},
            # {'exp_name':'food','mems':'vishal','mems_wal':6000,'share':200},
            # {'exp_name':'food','mems':'user1','mems_wal':7000,'share':300}]
                    elif(typ == 2):
                        for i in range(x):
                            name = input("ENTER THE MEM NAME: ")
                            share = int(input("ENTER HIS SHARE: "))
                            ne = {}
                            ng = {}
                            non_noti = {}
                            ng['name'] = username
                            ng['exp_name'] = expname
                            ng['mem'] = non_grpmem
                            ne['exp_name'] = expname
                            ne['expense_creater'] = username
                            ne['expense_amount'] = expamount
                            ne['paid_by'] = paidby
                            ne['mems'] = name
                            ne['share'] = share
                            ne['status'] = 'PENDING'
                            ne['date'] = None
                            for j in users:
                                if(j['name'] == name):
                                    ne['mems_wal'] = j['user_wallet']
                                    break
                            non_noti['exp_name'] = expname
                            non_noti['expense_creater'] = username
                            non_noti['expense_amount'] = expamount
                            non_noti['paid_by'] = paidby
                            non_noti['mems'] = name
                            non_noti['share'] = share
                            non_noti['status'] = 'PENDING'
                            non_noti['date'] = None
                            for j in users:
                                if(j['name'] == name):
                                    non_noti['mems_wal'] = j['user_wallet']
                                    break
                            non_grpmem.append(ne)
                            non_group.append(ng)
                            non_grpnotification.append(non_noti)
                        print(non_grpmem)
            elif(expencetype == 3):
                break
        elif(b == 4):
            os.system('cls')
            print("**********SETTLE UP*********\n")
            settleup(username)
        elif(b == 5):
            os.system('cls')
            print("**********WALLET BALANCE*********\n")
            bal(username)
        elif(b == 6):
            os.system('cls')
            print("**********HISTORY*********\n")
            his(username)
        elif(b == 7):
            os.system('cls')
            break


while(True):
    print("**********LOGIN**********\n")
    print("1.EXISTING USER\n2.NEW USER\n3.EXIT\n")
    a = int(input("ENTER YOUR CHOICE: "))
    if(a == 1):
        os.system('cls')
        mail = input("ENTER YOUR MAIL: ")
        passwd = input("ENTER YOUR PASSWD: ")
        for i in users:
            if(i['mail'] == mail and i['passwd'] == passwd):
                username = i['name']
                os.system('cls')
                print("LOGGED IN SUCCESSFULLY")
                time.sleep(1)
                os.system('cls')
                print("**********WELCOME", i['name'], "**********\n", sep="")
                userfun(username)
        else:
            print("USER NOT FOUND!")
    elif(a == 2):
        os.system('cls')
        name = input("ENTER YOUR NAME: ")
        mail = input("ENTER YOUR MAIL: ")
        passwd = input("ENTER YOUR PASSWD: ")
        wallet = int(input("ENTER YOUR WALLET AMOUNT: "))
        new = {}
        new['name'] = name
        new['mail'] = mail
        new['passwd'] = passwd
        new['user_wallet'] = wallet
        users.append(new)
        print("USER CREATED SUCCESSFULLY")
        input("PRESS ENTER TO CONTINUE.....")
    elif(a == 3):
        a = 'THANK YOU'
        for i in a:
            print(i, sep='')
            time.sleep(0.1)
        exit()
