import os
import random
import datetime
admins = [{'name': 'vijay', 'email': 'vijay@gmail.com', 'pass': '1234'}]
users = [{'name': 'user1', 'user_id': 1, 'email': 'user1@gmail.com',
          'pass': '1234', 'wallet': 1500, 'borrow_limit': 0},
         {'name': 'user2', 'user_id': 2, 'email': 'user2@gmail.com',
          'pass': '1234', 'wallet': 1500, 'borrow_limit': 0}, {'name': 'user3', 'user_id': 3, 'email': 'user3@gmail.com',
                                                               'pass': '1234', 'wallet': 1500, 'borrow_limit': 0}]
books = [{'name': 'python', 'isbn_no': 1000, 'price': 495, 'stock': 5, 'borrow': 0},
         {'name': 'chemistry', 'isbn_no': 1001, 'price': 495, 'stock': 10, 'borrow': 0}]
cart = []
id = []
unused = []
his = []
che = []
status = []


def randomnum():
    randomlist = []
    for i in range(1):
        n = random.randint(1000, 9000)
        randomlist.append(n)
    return randomlist[0]


for i in users:
    id.append(i['user_id'])


def management():
    while(True):
        os.system('cls')
        print("***********BOOK MANAGEMENT***********\n")
        print("1.ADD BOOK\n2.VIEW ALL BOOKS\n3.BOOK STOCK CHECK\n4.BOOK STOCK UPDATE\n5.BACK\n")
        b = int(input("ENTER YOUR CHOICE: "))
        if(b == 1):
            os.system('cls')
            newbooks = {}
            print("***********ADD BOOK***********\n")
            c = input("ENTER THE NAME OF THE NEW BOOK: ")
            d = randomnum()
            f = int(input("ENTER THE PRICE OF THE BOOK: "))
            e = int(input("ENTER THE STOCK OF THE NEW BOOK: "))
            print()
            newbooks['name'] = c
            newbooks['isbn_no'] = d
            newbooks['price'] = f
            newbooks['stock'] = e
            newbooks['borrow'] = 0
            books.append(newbooks)
            print("NEW BOOK ADDED SUCCESSFULLY\n")
            print("NAME: {}\nISBN NUMBER: {}\nPRICE: {}\nSTOCK: {}".format(c, d, f, e))
            print()
            input("PRESS ENTER TO CONTINUE.....")
        elif(b == 2):
            os.system('cls')
            print("***********VIEW BOOKS***********\n")
            for i in books:
                print("NAME: {}\nISBN NUMBER: {}\nPRICE {}\nSTOCK: {}".format(
                    i['name'], i['isbn_no'], i['price'], i['stock']))
                print('\n')
            input("PRESS ENTER TO CONTINUE.....")
        elif(b == 3):
            os.system('cls')
            print("***********STOCK CHECK***********\n")
            for i in books:
                print("NAME: {}\nISBN NUMBER: {}\nPRICE {}\nSTOCK: {}".format(
                    i['name'], i['isbn_no'], i['price'], i['stock']))
                print('\n')
            input("PRESS ENTER TO CONTINUE.....")
        elif(b == 4):
            os.system('cls')
            print("***********STOCK UPDATE***********\n")
            for i in books:
                print("NAME: {}\nISBN NUMBER: {}\nPRICE {}\nSTOCK: {}".format(
                    i['name'], i['isbn_no'], i['price'], i['stock']))
                print('\n')
            f = input("ENTER THE BOOK NAME TO UPDATE STOCK: ")
            for i in books:
                if(i['name'] == f):
                    n = int(input("ENTER THE STOCK TO ADD: "))
                    i['stock'] += n
                    print()
                    print("STOCK UPDATED SUCCESSFULLY\n")
                    input("PRESS ENTER TO CONTINUE.....")
                    break
            else:
                print("NO RESULT FOUND")
                input("PRESS ENTER TO CONTINUE.....")
        elif(b == 5):
            break


def user():
    os.system('cls')
    status_d = {}
    u = None
    x = input("ENTER YOUR USER MAIL: ")
    y = input("ENTER YOUR USER PASSWORD: ")
    flag = 0
    for i in users:
        if(x == i['email'] and y == i['pass']):
            u = i
            flag = 1
            while(True):
                os.system('cls')
                print("***********WELCOME USER***********\n")
                print(
                    "1.SEARCH BOOKS\n2.VIEW CHECKOUT CART\n3.BORROW BOOK\n4.BORROW HISTORY\n5.UPDATE BOOK STATUS\n6.WALLET BALANCE\n7.BACK\n")
                b = int(input("ENTER YOUR CHOICE: "))
                if(b == 1):
                    os.system('cls')
                    print("***********SEARCH BOOKS***********\n")
                    for i in books:
                        print("NAME: {}\nISBN NUMBER: {}\nPRICE {}".format(
                            i['name'], i['isbn_no'], i['price']))
                    print()
                    print("1.SEARCH BY NAME\n2.SEARCH BY ISBN NUMBER\n3.BACK\n")
                    c = int(input("ENTER YOUR CHOICE: "))
                    if(c == 1):
                        os.system('cls')
                        d = input("ENTER THE BOOK NAME: ")
                        for i in books:
                            if(i['name'] == d):
                                os.system('cls')
                                print("NAME: {}\nPRICE: {}".format(
                                    i['name'], i['price']))
                                print()
                                print("1.ADD TO CHECKOUT CART\n2.BACK\n")
                                e = int(input("ENTER YOUR CHOICE: "))
                                if(e == 1):
                                    cart.append(i)
                                    print('ADDED TO CHECKOUT CART SUCCESSFULLY\n')
                                    input("PRESS ENTER TO CONTINUE.....")
                                elif(e == 2):
                                    break
                    elif(c == 2):
                        os.system('cls')
                        d = int(input("ENTER THE BOOK ISBN NUMBER: "))
                        for i in books:
                            if(i['isbn_no'] == d):
                                os.system('cls')
                                print("NAME: {}\nPRICE: {}".format(
                                    i['name'], i['price']))
                                print()
                                print("1.ADD TO CHECKOUT CART\n2.BACK\n")
                                e = int(input("ENTER YOUR CHOICE: "))
                                if(e == 1):
                                    cart.append(i)
                                    print('ADDED TO CHECKOUT CART SUCCESSFULLY\n')
                                    input("PRESS ENTER TO CONTINUE.....")
                                elif(e == 2):
                                    break
                elif(b == 2):
                    os.system('cls')
                    print("***********CHECKOUT CART***********\n")
                    for i in cart:
                        print("NAME: {}\nPRICE: {}".format(
                            i['name'], i['price']))
                        print()
                    print("1.BORROW\n2.BACK\n")
                    f = int(input("ENTER YOUR CHOICE: "))
                    if(f == 1):
                        os.system('cls')
                        print("***********BORROW***********\n")
                        y = input("ENTER THE BOOK NAME: ")
                        for i in books:
                            if(y not in che):
                                if(y == i['name']):
                                    if(i['stock'] > 0):
                                        i['stock'] -= 1
                                        if(u['borrow_limit'] <= 2):
                                            limit = u['borrow_limit']+1
                                            u['borrow_limit'] = limit
                                            if(u['wallet'] >= 500):
                                                p = i['borrow']+1
                                                i['borrow'] = p

                                                print(
                                                    "BORROWED SUCCESSFULLY\n")
                                                status_d['book_name'] = i['name']
                                                status_d['User_name'] = u['name']
                                                status_d['Borrow Date'] = d
                                                status_d['Due Date'] = d + \
                                                    datetime.timedelta(days=14)
                                                status_d['Status'] = 'Borrowed'
                                                status.append(status_d)
                                                print(
                                                    "NOTE: IF THE BOOK IS NOT RETURNED FINE WILL BE COLLECTED!.....")
                                                his.append(i)
                                                che.append(y)
                                                input(
                                                    "PRESS ENTER TO CONTINUE.....")
                                                break
                                            else:
                                                print(
                                                    "INSUFFICIENT BALANCE IN WALLET")
                                                input(
                                                    "PRESS ENTER TO CONTINUE.....")
                                                os.system('cls')
                                                break
                                        else:
                                            print(
                                                "BORROW LIMIT HAS BEEN REACHED")
                                            input(
                                                "PRESS ENTER TO CONTINUE.....")
                                            os.system('cls')
                                            break
                                    else:
                                        print("BOOK OUT OF STOCK")
                                        input("PRESS ENTER TO CONTINUE.....")
                                        os.system('cls')
                                        break
                            else:
                                print("BOOK ALREADY BROUGHT")
                                input("PRESS ENTER TO CONTINUE.....")
                                os.system('cls')
                                break
                        else:
                            print("NO RESULT FOUND")
                            input("PRESS ENTER TO CONTINUE.....")
                            os.system('cls')
                elif(b == 3):
                    os.system('cls')
                    print("***********BORROW***********\n")
                    y = input("ENTER THE BOOK NAME: ")
                    for i in books:
                        if(y not in che):
                            if(y == i['name']):
                                if(i['stock'] > 0):
                                    i['stock'] -= 1
                                    if(u['borrow_limit'] <= 2):
                                        limit = u['borrow_limit']+1
                                        u['borrow_limit'] = limit
                                        if(u['wallet'] >= 500):
                                            p = i['borrow']+1
                                            i['borrow'] = p
                                            d=datetime.datetime.now()
                                            print(
                                                "BORROWED SUCCESSFULLY\n")
                                            status_d['book_name'] = i['name']
                                            status_d['User_name'] = u['name']
                                            status_d['Borrow Date'] = d
                                            status_d['Due Date'] = d + \
                                                datetime.timedelta(days=14)
                                            status_d['Status'] = 'Borrowed'
                                            status.append(status_d)
                                            print(
                                                "NOTE: IF THE BOOK IS NOT RETURNED FINE WILL BE COLLECTED!.....")
                                            his.append(i)
                                            che.append(y)
                                            input(
                                                "PRESS ENTER TO CONTINUE.....")
                                            break
                                        else:
                                            print(
                                                "INSUFFICIENT BALANCE IN WALLET")
                                            input(
                                                "PRESS ENTER TO CONTINUE.....")
                                            os.system('cls')
                                            break
                                    else:
                                        print(
                                            "BORROW LIMIT HAS BEEN REACHED")
                                        input(
                                            "PRESS ENTER TO CONTINUE.....")
                                        os.system('cls')
                                        break
                                else:
                                    print("BOOK OUT OF STOCK")
                                    input("PRESS ENTER TO CONTINUE.....")
                                    os.system('cls')
                                    break
                        else:
                            print("BOOK ALREADY BROUGHT")
                            input("PRESS ENTER TO CONTINUE.....")
                            os.system('cls')
                            break
                    else:
                        print("NO RESULT FOUND")
                        input("PRESS ENTER TO CONTINUE.....")
                        os.system('cls')
                elif(b == 4):
                    os.system('cls')
                    print("***********BORROW HISTORY***********\n")
                    if(len(his) > 0):
                        for i in his:
                            print(i)
                        input("PRESS ENTER TO CONTINUE.....")
                    else:
                        print("NO HISTORY")
                        input("PRESS ENTER TO CONTINUE.....")
                elif(b == 5):
                    os.system('cls')
                    print("***********UPDATE BOOK STATUS***********\n")
                    print("1.UPDATE BOOK STATUS\n2.EXIT")
                    a = int(input("Enter choice : "))
                    if(a == 1):
                        for i in status:
                            if(i['User_name'] == u['name']):
                                print("BOOK NAME : {}\nUSERNSME :{}\nBORROW DATE :{}\nDUE DATE :{}\nSTATUS : {}".format(
                                    i['book_name'], i['User_name'], i['Borrow Date'], i['Due Date'], i['Status']))
                                print()
                        for i in status:
                            if(i['User_name'] == u['name']):
                                c = input("Enter Book name : ")
                                if(i['book_name'] == c):
                                    for k in books:
                                        if(k['name'] == c):
                                            amount = k['price']
                                            print("1.RETURN BOOK\n2.LOST BOOK")
                                            b = int(input("Enter choice : "))
                                            if(b == 1):
                                                i['Status'] = "RETURNED"
                                                k['stock'] += 1
                                                print(
                                                    "STATUS UPDATED SUCCESSFULLY")
                                                input(
                                                    "PRESS ENTER TO CONTINUE.....")
                                                break

                                            elif(b == 2):
                                                i['Status'] = "LOST"
                                                for j in users:
                                                    ans = amount/2
                                                    j['wallet'] -= ans
                                                    print(
                                                        "SINCE THE BOOKS IS LOST AS PER THE RULE\nTHE HALF OF THE PRICE IS COLLECTED AS A FINE\nTHE ACTUAL PRICE IS", amount)
                                                    break
                                                print(
                                                    "STATUS UPDATED SUCCESSFULLY")
                                                input(
                                                    "PRESS ENTER TO CONTINUE.....")
                                                break
                elif(b==6):
                    print("***********WALLET BALANCE***********\n")
                    print("1.CHECK WALLET BALANCE\n2.EXIT")
                    g=int(input("ENTER YOU CHOICE: "))
                    if(g==1):
                        for i in users:
                            print("YOUR WALLET BALANCE IS",u['wallet'])
                            input("PRESS ENTER TO CONTINUE.....")
                            break
                    elif(g==2):
                        break                    
                elif(b == 7):
                    che.clear()
                    his.clear()
                    break

    if(flag == 0):
        print("MAIL AND PASSWORD DOES NOT MATCH")


def admin():
    os.system('cls')
    print("***********WELCOME ADMIN***********\n")
    name = input("ENTER YOUR EMAIL: ")
    passwd = input("ENTER YOUR PASSWORD: ")
    for i in admins:
        if(name == i['email'] and passwd == i['pass']):
            while(True):
                os.system('cls')
                print("***********WELCOME ADMIN***********\n")
                print("1.ADD ADMIN\n2.ADD USER\n3.BOOK MANAGEMENT\n4.REPORTS\n5.BACK\n")
                ch = int(input("ENTER YOUR CHOICE: "))
                if(ch == 1):
                    os.system('cls')
                    newadmin = {}
                    print("***********ADD ADMIN***********\n")
                    b = input("ENTER THE NEW ADMIN NAME: ")
                    c = input("ENTER THE NEW ADMIN EMAIL: ")
                    d = input("ENTER THE NEW ADMIN PASSWD: ")
                    print()
                    newadmin['name'] = b
                    newadmin['email'] = c
                    newadmin['pass'] = d
                    admins.append(newadmin)
                    print("NEW ADMIN ADDED SUCCESSFULLY\n")
                    input("PRESS ENTER TO CONTINUE.....")
                    os.system('cls')
                elif(ch == 2):
                    os.system('cls')
                    newuser = {}
                    print("***********ADD USER***********\n")
                    e = input("ENTER THE NEW USER NAME: ")
                    f = input("ENTER THE NEW USER EMAIL: ")
                    g = input("ENTER THE NEW USER PASSWORD: ")
                    print()
                    newuser['name'] = e
                    newuser['user_id'] = id[-1]+1
                    newuser['email'] = f
                    newuser['pass'] = g
                    users.append(newuser)
                    print("NEW USER SUCCESSFULLY ADDED\n")
                    print("NAME: {}, ID: {}, MAIL: {}, PASSWORD: {}".format(
                        newuser['name'], newuser['user_id'], newuser['email'], newuser['pass']))
                    print()
                    input("PRESS ENTER TO CONTINUE.....")
                    os.system('cls')
                elif(ch == 3):
                    management()
                elif(ch == 4):
                    os.system('cls')
                    print("***********REPORT***********\n")
                    print(
                        "1.QUANTITY\n2.UNUSED BOOKS\n3.HIGHLY USED BOOKS\n4.STATUS OF BOOKS\n5.BACK\n")
                    h = int(input("ENTER YOUR CHOICE: "))
                    while(True):
                        if(h == 1):
                            os.system('cls')
                            print("***********QUANTIY***********\n")
                            k = []
                            for i in books:
                                k.append(i['stock'])
                            k.sort()
                            for i in books:
                                if(k[0] == i['stock']):
                                    print("NAME: {}\nISBN NUMBER: {}\nSTOCK: {}\n".format(
                                        i['name'], i['isbn_no'], i['stock']))
                                    print("KINDLY UPDATE THE STOCK")
                                    input("PRESS ENTER TO CONTINUE.....")
                            break
                        elif(h == 2):
                            os.system('cls')
                            print("***********UNUSED BOOKS***********\n")
                            for i in books:
                                if(i['borrow'] == 0):
                                    unused.append(i)
                            if(len(unused) > 0):
                                for i in unused:
                                    print("NAME: {}\nISBN NUMBER: {}\nSTOCK: {}\n".format(
                                        i['name'], i['isbn_no'], i['stock']))
                            else:
                                print("NO UNUSED BOOKS")
                            unused.clear()
                            input("PRESS ENTER TO CONTINUE.....")
                            break
                        elif(h == 3):
                            os.system('cls')
                            print("***********HIGHLY USED BOOKS***********\n")
                            p = []
                            for i in books:
                                p.append(i['borrow'])
                            max_p = max(p)
                            for i in books:
                                if(i['borrow'] == max_p):
                                    cb = i
                                    print("NAME: {}\nISBN NUMBER: {}\n".format(
                                        i['name'], i['isbn_no']))
                                    while(True):
                                        print("1.CHECK CONDITION\n2.SKIP\n")
                                        o = int(input("ENTER YOUR CHOICE: "))
                                        if(o == 1):
                                            print("NAME: {}\nISBN NUMBER: {}\n".format(
                                                cb['name'], cb['isbn_no']))
                                            print("1.GOOD\n2.BAD\n")
                                            q = int(
                                                input("ENTER YOUR CHOICE: "))
                                            if(q == 1):
                                                pass
                                                print(
                                                    "CONDITION UPDATED SUCCESSFULLY")
                                                input(
                                                    "PRESS ENTER TO CONTINUE.....")
                                                break
                                            elif(q == 2):
                                                print(
                                                    "THE BOOK HAS BEEN REMOVED BECAUSE OF BAD CONDITION")
                                                cb['stock'] -= 1
                                                input(
                                                    "PRESS ENTER TO CONTINUE.....")
                                                break
                                        elif(o == 2):
                                            input(
                                                "PRESS ENTER TO CONTINUE.....")
                                            break
                            else:
                                print("NO HIGH BORROWED BOOKS")
                                input("PRESS ENTER TO CONTINUE.....")
                                break

                        elif(h == 4):
                            print("***********STATUS OF BOOKS***********\n")
                            print("1.CHECK STATUS\n2.EXIT")
                            f=int(input("ENTER YOUR CHOICE: "))
                            if(f==1):
                                if(len(status)!=0):
                                    for i in status:
                                        print("BOOK NAME: {}\nUSERNAME: {}\nBORROW DATE: {}\nDUE DATE: {}\nSTATUS: {}".format(i['book_name'],i['User_name'],i['Borrow Date'],i['Due Date'],i['Status']))
                                        print() 
                                else:
                                    print("NO DATA FOUND")
                            elif(f==2):
                                break
                        elif(h==5):
                            break

                elif(ch == 5):
                    os.system('cls')
                    break


print("***********WELCOME TO LIBRARY***********\n")

while(True):
    print("1.ADMIN\n2.USER\n3.EXIT\n")
    a = int(input("ENTER YOUR CHOICE: "))
    if(a == 1):
        admin()
    elif(a == 2):
        user()
    elif(a == 3):
        exit()
