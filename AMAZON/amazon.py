import os
import datetime
g_product_id = 22
admin = [{'ad_name': 'Admin1', 'passwd': 'admin1'}]
merchant = [{'m_name': 'Merchant1', 'passwd': 'merchant1', 'status': 'APPROVED'},
            {'m_name': 'Merchant2', 'passwd': 'merchant2', 'status': 'APPROVED'}]
buyer = [{'b_name': 'vijay', 'passwd': 'vijay98430', 'wallet': 100000, 'order_count': 0},
         {'b_name': 'vijay', 'passwd': 'vijay98430', 'wallet': 100000, 'order_count': 0}]
product = [{'pro_merch': 'Merchant1', 'pro_brand': 'fasttrack', 'pro_name': 'smartwatch', 'price': 20000, 'stock': 100, 'discount': 50, 'review': "", 'category': 'electronics'},
           {'pro_merch': 'Merchant1', 'pro_brand': 'fasttrack', 'pro_name': 'headset',
               'price': 200, 'stock': 120, 'discount': 30, 'review': "", 'category': 'accessories'},
           {'pro_merch': 'Merchant1', 'pro_brand': 'fastrack', 'pro_name': 'laptop',
               'price': 52000, 'stock': 50, 'discount': 40, 'review': "", 'category': 'electronics'},
           {'pro_merch': 'Merchant1', 'pro_brand': 'fastrack', 'pro_name': 'snekers',
               'price': 900, 'stock': 50, 'discount': 40, 'review': "", 'category': 'fashion'},
           {'pro_merch': 'Merchant2', 'pro_brand': 'apple', 'pro_name': 'Iphone 13',
               'price': 78900, 'stock': 15, 'discount': 20, 'review': "", 'category': 'mobile'},
           {'pro_merch': 'Merchant2', 'pro_brand': 'apple', 'pro_name': 'airpod', 'price': 10000,
               'stock': 70, 'discount': 45, 'review': "", 'category': 'accessories'},
           {'pro_merch': 'Merchant2', 'pro_brand': 'apple', 'pro_name': 'laptop', 'price': 60000, 'stock': 8, 'discount': 20, 'review': "", 'category': 'electronics'}]
new_merchants = []
cart = []
cat = ['electronics', 'accessories', 'mobile', 'fashion']
order_his = []
totalorder = []
salesreview = []


def review(mcr):
    while(True):
        print("1.PRODUCT REVIEWS\n2.CUSTOMER REVIEWS\n3.SALES REVIEW\n4.EXIT")
        a = int(input("ENTER YOUR CHOICE: "))
        if(a == 1):
            for i in product:
                if(i['pro_merch'] == mcr):
                    print("PRODUCT NAME: {}, REVIEWS: {} ,AVAILABLE STOCK {}".format(
                        i['pro_name'], i['review'],i['stock']))
        elif(a == 2):
            ans = []
            print(totalorder)
            for i in totalorder:
                if(i['pro_merch'] == mcr):
                    ans.append(i)
            for i in ans:
                print(i, sep="\n")
        elif(a == 3):
            print(salesreview)
            for i in salesreview:
                if(i['pro_merch'] == mcr):
                    print("USER NAME: {},PRODUCT NAME: {}, PRICE: {}, DATE: {}".format(
                        i['b_name'], i['pro_name'], i['price'], i['date']))
            else:
                print("NO SALES HAS BEEN RECORDED")
        elif(a == 4):
            break


def history():
    if(len(order_his) > 0):
        for i in order_his:
            print(i, sep='\n')
    else:
        print("NO ORDER HISTORY FOUND")


def walbal(user):
    print("YOUR CURRENT WALLET BALANCE IS: ", user['wallet'])


def proorder(user):
    freq_customer = {}
    sales = {}
    while(True):
        print("1.SELECT FROM CART\n2.SELECT FROM SEARCH\n3.Exit")
        u = int(input("ENTER YOUR CHOICE TO ORDER: "))
        if(u == 1):
            if(len(cart) > 0):
                for i in cart:
                    print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
                    print("\n")
                name = input("ENTER THE PRODUCT NAME: ")
                for i in cart:
                    if(i['pro_name'] == name):
                        print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
                        print("\n")
                        print("PRESS 'Y' TO PLACE THE ORDER 'N' TO CANCEL ")
                        v = input("ENTER YOUR CHOICE: ")
                        if(v == 'y' or 'Y'):
                            if(i['price'] <= user['wallet']):
                                dis = i['price']*(i['discount']/100)
                                user['wallet'] -= i['price']-dis
                                i['stock'] -= 1
                                print("ORDER PLACED SUCCESSFULLY")
                                user['order_count'] += 1
                                ordercount = user['order_count']
                                merchname = i['pro_merch']
                                username = user['b_name']
                                productprice = i['price']
                                proname = i['pro_name']
                                dt = datetime.datetime.now()
                                freq_customer['pro_merch'] = merchname
                                freq_customer['b_name'] = username
                                freq_customer['order_count'] = ordercount
                                totalorder.append(freq_customer)
                                order_his.extend(["PRODUCT BRAND: {}, \nPRODUCT NAME: {}, \nPRICE: {}, \nDATE: {}".format(
                                    i['pro_brand'], i['pro_name'], i['price'], dt)])

                                sales['pro_merch'] = merchname
                                sales['pro_name'] = proname
                                sales['b_name'] = username
                                sales['price'] = productprice
                                sales['date'] = dt
                                salesreview.append(sales)
                                while(True):
                                    print("1.REVIEW\n2.LATER")
                                    b = int(input("ENTER YOUR CHOICE TO REVIEW: "))
                                    if(b == 1):
                                        c = input("GIVE YOUR REVIEW: ")
                                        i['review'] = c
                                        break
                                    elif(b == 2):
                                        break
                            else:
                                print(
                                    "INSUFFICIENT BALANCE IN WALLET TO PLACE THE ORDER\nKINDLY RECHARGE YOUR WALLET")
                        elif(v == 'n' or 'N'):
                            break
                else:
                    print("NO RESULT FOUND")
                    break
            else:
                print("NO ITEM IN CART")
        elif(u == 2):
            l = []
            name = input("ENTER THE PRODUCT NAME TO SEARCH: ")
            for i in product:
                if(name == i['pro_name']):
                    l.append(i)
            if(len(l) > 0):
                pass
            else:
                print("NO RESULT FOUND")
            print(*l)
            for i in l:
                os.system('cls')
                print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
                print("\n")
                print("1.ORDER\n2.NEXT\n3.EXIT")
                n = int(input("ENTER YOUR CHOICE TO ORDER: "))
                if(n == 1):
                    print("ENTER Y TO PLACE THE ORDER,ENTER N TO CANCEL")
                    a = input("ENTER YOUR CHOICE TO ORDER: ")
                    if(a == 'y' or 'Y'):
                        if(i['price'] <= user['wallet']):
                            dis = i['price']*(i['discount']/100)
                            user['wallet'] -= i['price']-dis
                            i['stock'] -= 1
                            print("ORDER PLACED SUCCESSFULLY")
                            user['order_count'] += 1
                            ordercount = user['order_count']
                            merchname = i['pro_merch']
                            username = user['b_name']
                            proname = i['pro_name']
                            productprice = i['price']
                            freq_customer['pro_merch'] = merchname
                            freq_customer['b_name'] = username
                            freq_customer['order_count'] = ordercount
                            totalorder.append(freq_customer)
                            dt = datetime.datetime.now()
                            sales['pro_merch'] = merchname
                            sales['b_name'] = username
                            sales['pro_name'] = proname
                            sales['price'] = productprice
                            sales['date'] = dt
                            salesreview.append(sales)
                            order_his.extend(["PRODUCT BRAND: {}, \nPRODUCT NAME: {}, \nPRICE: {}, \nDATE: {}%".format(
                                i['pro_brand'], i['pro_name'], i['price'], dt)])
                            print("1.REVIEW\n2.LATER")
                            b = int(input("ENTER YOUR CHOICE TO REVIEW: "))
                            if(b == 1):
                                c = input("GIVE YOUR REVIEW: ")
                                i['review'] = c
                                break
                            elif(b == 2):
                                break
                            l.remove(i)
                            break
                elif(n == 2):
                    pass
                elif(n == 3):
                    break
            else:
                print("NO MORE RESULT IN", name)
            l.clear()
        elif(u == 3):
            break


def procart():
    os.system('cls')
    if(len(cart)>0):
        for i in cart:
            print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nSTOCK : ",i['stock'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
            print("\n")
    else:
        print("NO ITEM ADDED")


def discount():
    b = []
    saving = 0
    while (True):
        print("1.SHOW\n2.EXIT")
        n = int(input("ENTER YOUR CHOICE TO PROCEED: "))
        if(n == 1):
            q = input("ENTER THE PRODUCT NAME: ")
            r = int(input("ENTER THE PRICE THAT YOU ARE LOOKING FOR: "))
            for i in product:
                if(q == i['pro_name'] and i['price'] <= r):
                    s = i['price']*(i['discount']/100)
                    saving = s
                    b.extend(["PRODUCT BRAND: {}, PRODUCT NAME: {}, YOU CAN SAVE RUPEES: {}".format(
                        i['pro_brand'], i['pro_name'], saving)])
            if(len(b) > 0):
                pass
            else:
                print("NO RESULT")
            for i in b:
                print(*i, sep='')
            b.clear()
            saving = 0
        elif(n == 2):
            break


def price():
    b = []
    while (True):
        print("1.SHOW\n2.EXIT")
        n = int(input("ENTER YOUR CHOICE TO PROCEED: "))
        if(n == 1):
            q = input("ENTER THE PRODUCT NAME: ")
            r = int(input("ENTER THE PRICE THAT YOU ARE LOOKING FOR: "))
            for i in product:
                if(q == i['pro_name'] and i['price'] <= r):
                    b.append(i)
            if(len(b) > 0):
                pass
            else:
                print("NO RESULT")
            print(*b)
            b.clear()
        elif(n == 2):
            break


def pro():
    p = []
    while (True):
        print("1.SHOW\n2.EXIT")
        n = int(input("ENTER YOUR CHOICE TO PROCEED: "))
        if(n == 1):
            q = input("ENTER THE BRAND NAME: ")
            for i in product:
                if(q == i['pro_name']):
                    p.append(i)
            if(len(p) > 0):
                pass
            else:
                print("NO RESULT")
            print(*p)
            p.clear()
        elif(n == 2):
            break


def brand():
    b = []
    while (True):
        print("1.SHOW\n2.EXIT")
        n = int(input("ENTER YOUR CHOICE TO PROCEED: "))
        if(n == 1):
            q = input("ENTER THE PRODUCT NAME: ")
            for i in product:
                if(q == i['pro_brand']):
                    b.append(i)
            if(len(b) > 0):
                pass
            else:
                print("NO RESULT")
            print(*b)
            b.clear()
        elif(n == 2):
            break


def userfilter():
    while(True):
        print("1.FILTER BY BRAND\n2.FILTER BY PRODUCT\n3.FILTER BY PRICE\n4.FILTER BY DISCOUNT\n5.EXIT")
        p = int(input("ENTER YOUR CHOICE BUYER TO FILTER: "))
        if(p == 1):
            print("FILTER BY BRAND")
            brand()
        elif(p == 2):
            print("FILTER BY PRODUCT")
            pro()
        elif(p == 3):
            print("FILTER BY PRICE")
            price()
        elif(p == 4):
            print("FILTER BY DISCOUNT")
            discount()
        elif(p == 5):
            break


def usersearch():
    l = []
    name = input("ENTER THE PRODUCT NAME TO SEARCH: ")
    for i in product:
        if(name == i['pro_name']):
            l.append(i)
    if(len(l) > 0):
        pass
    else:
        print("NO RESULT FOUND")
    print(*l)
    for i in l:
        os.system('cls')
        print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nSTOCK : ",i['stock'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
        print("\n")
        print("1.ADD TO CART\n2.NEXT\n3.EXIT")
        n = int(input("ENTER YOUR CHOICE TO ADD TO CART: "))
        if(n == 1):
            print("ADDED TO CART SUCCESSFULLY")
            cart.append(i)
        elif(n == 2):
            pass
        elif(n == 3):
            break
    else:
        ("NO MORE RESULT IN", name)
    l.clear()


def stockupdate(mcr):
    while(True):
        print("1.UPDATE\n2.EXIT")
        n = int(input("ENTER YOUR CHOICE MERCHANT TO UPDATE: "))
        if(n == 1):
            name = input("ENTER THE PRODUCT NAME TO UPDATE: ")
            for i in product:
                if(i['pro_merch'] == mcr):
                    if(i['pro_name'] == name):
                        o = int(input("ENTER THE STOCK TO UPDATE: "))
                        i['stock'] += o
                        break
            else:
                print("PRODUCT NOT FOUND")

        elif(n == 2):
            break


def stockcheck(mcr):
    while(True):
        print("1.CHECK\n2.EXIT")
        m = int(input("ENTER YOUR CHOICE MERCHANT TO CHECK: "))
        if(m == 1):
            for i in product:
                if(i['pro_merch'] == mcr):
                    print("PRODUCT NAME : ",i['pro_name'],"\nSTOCK : ",i['stock'])
                    print("\n")
        elif(m == 2):
            break


def removepro(mcr):
    while(True):
        print("1.REMOVE\n2.EXIT")
        l = int(input("ENTER YOUR CHOICE MERCHANT TO REMOVE: "))
        if(l == 1):
            name = input("ENTER THE PRODUCT NAME TO BE REMOVED: ")
            for i in product:
                if(i['pro_merch'] == mcr):
                    if(i['pro_name'] == name):
                        product.remove(i)
                        break
            else:
                print("MERCHANT NOT FOUND")
        elif(l == 2):
            break


def showpro(mcr):
    for i in product:
        if(i['pro_merch'] == mcr):
            print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nSTOCK : ",i['stock'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
            print("\n")

def addpro(mcr):
    while(True):
        newpro = {}
        flag = 0
        print("1.ADD\n2.EXIT")
        k = int(input("ENTER YOUR CHOICE MERCHANT TO ADD: "))
        if(k == 1):
            productmerch = mcr
            productbrand = input("ENTER THE BRAND NAME: ")
            productname = input("ENTER THE PRODUCT NAME: ")
            productprice = int(input("ENTER THE PRICE OF THE PRODUCT: "))
            productstock = int(input("ENTER THE PRODUCT STOCK: "))
            productreview = ""
            productcategory = input("ENTER THE PRODUCT CATEGORY: ")
            if(productcategory in cat):
                for i in product:
                    if(productname not in i['pro_name']):
                        flag += 1
            else:
                print("CURRENT PRODUCT CATEGORY IS NOT ALLOWED")
                break
            if(flag == len(product)):
                newpro['pro_merch'] = productmerch
                newpro['pro_brand'] = productbrand
                newpro['pro_name'] = productname
                newpro['price'] = productprice
                newpro['stock'] = productstock
                newpro['review'] = productreview
                newpro['category'] = productcategory
                product.append(newpro)
                print("NEW PRODUCT ADDED SUCCESSFULLY")
            else:
                print(
                    "PRODUCT NAME ALREADY EXIST\nYOU CANNOT ADD ANOTHER PRODUCT WITH SAME NAME")
        elif(k == 2):
            break


def showmerch():
    for i in merchant:
        print("Merchant name : {},\nStatus :{}".format(i['m_name'],i['status']))
        print("\n")

def removemerch():
    while(True):
        print("1.REMOVE\n2.BACK")
        h = int(input("ENTER YOUR CHOICE: "))

        if(h == 1):
            name = input("ENTER THE MERCHANT NAME TO BE REMOVED: ")
            for i in merchant:
                if(i['m_name'] == name):
                    i['status'] = 'REMOVED'
                    print("REMOVED SUCCESSFULLY")
                    break
            else:
                print("NO SUCH MERCHANT FOUND")
        elif(h == 2):
            break


def addmerch():
    while(True):
        print("1.ADD\n2.BACK")
        new_merch = {}
        g = int(input("ENTER YOUR CHOICE: "))
        flag = 1
        if(g == 1):
            name = input("ENTER NEW MERCH NAME: ")
            passwd = input("ENTER NEW MERCH PASSWORD: ")
            status = 'APPROVED'
            for i in merchant:
                if(name == i["m_name"]):
                    flag = 0
            if(flag == 1):
                new_merch['m_name'] = name
                new_merch['passwd'] = passwd
                new_merch['status'] = status
                merchant.append(new_merch)
                print("Merchant added succesfully")
            else:
                print("TRY DIFFERENT NAME")

        elif(g == 2):
            break


# merchant approval

def approve():
    print("1.APPROVE\n2.REJECT")
    if(len(new_merchants) > 0):
        for i in new_merchants:
            print(i['m_name'])
            g = int(input("ENTER YOUR CHOICE TO APPROVE: "))
            if(g == 1):
                i['status'] = 'APPROVED'
            elif(g == 2):
                i['status'] = 'REJECTED'
    else:
        print("NO MORE REQUEST")
    new_merchants.clear()

# admins verfication


def admins():

    name = input("ENTER YOUR NAME ADMIN: ")
    passwd = input("ENTER YOUR PASSWORD: ")
    for i in admin:
        if(name == i['ad_name'] and passwd == i['passwd']):
            os.system('cls')
            print("WELCOME", i['ad_name'])
            
            while(True):
                print(
                "1.ADD MERCHANT\n2.REMOVE MERCHANT\n3.APPROVE MERCHANT\n4.SHOW MERCHANTS\n5.VIEW PRODUCTS\n6.ADD CATEGORY\n7.LOGOUT")
                b = int(input("ENTER YOUR CHOICE ADMIN: "))
                if(b == 1):
                    os.system('cls')
                    print("ADD MERCHANT")
                    addmerch()
                elif(b == 2):
                    os.system('cls')
                    print("REMOVE MERCHANT")
                    removemerch()
                elif(b == 3):
                    os.system('cls')
                    print("APPROVE MERCAHNT")
                    approve()
                elif(b == 4):
                    os.system('cls')
                    print("ALL MERCHANTS")
                    showmerch()
                elif(b == 5):
                    print("PRODUCT")
                    for i in product:
                        print("MERCHANT NAME : ",i['pro_merch'],"\nBRAND NAME : ",i['pro_brand'],"\nPRODUCT_NAME :",i['pro_name'],"\nAMOUNT: ",i['price'],"\nSTOCK : ",i['stock'],"\nDISCOUNT:",i['discount'],"\nCATEGORY : ",i['category'])
                        print("\n")
                elif(b == 6):
                    
                    for i in cat:
                        print("Category : ",i)
                    a = input("ENTER THE CATEGORY TO BE ADDED: ")
                    if(a not in cat):
                        print("PRESS Y TO CONFIRM\nPRESS N TO CANCEL")
                        c = input("ENTER YOUR CHOICE: ")
                        if(c == 'y' or 'Y'):
                            cat.append(a)
                            print("NEW CATEGORY ADDED")
                    else:
                        print("PRODUCT CATEGORY ALREADY EXIST")

                elif(b == 7):
                    break
                else:
                    print("INVALID CHOICE ADMIN")
        else:
            print("ADMIN NOT FOUND")
            break

# merchants verfication


def merchants():

    name = input("ENTER YOUR NAME MERCHANT: ")
    passwd = input("ENTER YOUR PASSWORD: ")
    mcr = None
    val = 0

    for i in merchant:
        if(name == i['m_name'] and passwd == i['passwd'] and i['status'] == 'APPROVED'):
            mcr = i['m_name']
            val = 1
        elif(name == i['m_name'] and passwd == i['passwd'] and i['status'] == 'REJECTED'):
            print("YOUR ACCOUNT HAS BEEN REJECTED")
            break
        elif(name == i['m_name'] and passwd == i['passwd'] and i['status'] == 'REMOVED'):
            print("YOUR ACCOUNT HAS BEEN REMOVED\nPLEASE CONTACT THE ADMIN")
            break
        elif(name == i['m_name'] and passwd == i['passwd'] and i['status'] == 'PENDING'):
            print("YOUR APPROVAL IS STILL IN PENDING\nKINDLY WAIT")
            break
        else:
            continue
    else:
        os.system('cls')
        if(val == 1):
            print("WELCOME", mcr)
            
            while(True):
                print(
                "1.ADD PRODUCT\n2.REMOVE PRODUCT\n3.STOCK UPDATE\n4.STOCK CHECK\n5.SHOW PRODUCTS\n6.VIEW REVIEWS\n7.LOGOUT")
                e = int(input("ENTER YOUR CHOICE MERCHANT: "))
                if(e == 1):
                    os.system('cls')
                    print("ADD PRODUCT")
                    addpro(mcr)
                elif(e == 2):
                    os.system('cls')
                    print("REMOVE PRODUCT")
                    removepro(mcr)
                elif(e == 3):
                    os.system('cls')
                    print("STOCK UPDATE")
                    stockupdate(mcr)
                elif(e == 4):
                    os.system('cls')
                    print("STOCK CHECK")
                    stockcheck(mcr)
                elif(e == 5):
                    os.system('cls')
                    print("ALL PRODUCTS")
                    showpro(mcr)
                elif(e == 6):
                    os.system('cls')
                    review(mcr)
                elif(e == 7):
                    break
                else:
                    print("INVALID CHOICE")
        elif(val == 0):
            while(True):
                print("1.REQUEST TO APPROVE\n2.EXIT")
                f = int(input("ENTER YOUR CHOICE MERCHANT: "))
                if(f == 1):
                    m_details = {}
                    name = input("ENTER NEW MERCAHNT NAME: ")
                    passwd = input("ENTER NEW MERCHANT PASSWORD: ")
                    flag = 1
                    for i in merchant:
                        if(name == i["m_name"]):
                            flag = 0
                    if(flag == 1):
                        m_details['m_name'] = name
                        m_details['passwd'] = passwd
                        m_details['status'] = 'PENDING'
                        new_merchants.append(m_details)
                        merchant.append(m_details)
                    else:
                        print("TRY DIFFERENT NAME")

                elif(f == 2):
                    break
                else:
                    print("INVALID CHOICE")
# buyer verfication


def buyers():
    user = None
    while(True):
        print("1.EXISTING USER\n2.NEW USER\n3.EXIT")
        d = int(input("ENTER YOUR CHOICE BUYER: "))
        if(d == 1):
            name = input("ENTER YOUR NAME BUYER: ")
            passwd = input("ENTER YOUR PASSWORD: ")
            for i in buyer:
                if(name == i['b_name'] and passwd == i['passwd']):
                    user = i
                    print("WELCOME", i['b_name'])
                    
                    while(True):
                        print(
                        "1.SEARCH\n2.FILTER\n3.ORDER\n4.VIEW CART\n5.WALLET BALANCE\n6.ORDER HISTORY\n7.LOGOUT")
                        print("\n")
                        e = int(input("ENTER YOUR CHOICE:"))
                        if(e == 1):
                            print("SEARCH")
                            usersearch()
                        elif(e == 2):
                            print("FILTER")
                            userfilter()
                        elif(e == 3):
                            print("ORDER")
                            proorder(user)
                        elif(e == 4):
                            print("CART")
                            procart()
                        elif(e == 5):
                            print("WALLET BALANCE")
                            walbal(user)
                        elif(e == 6):
                            print("HISTORY")
                            history()
                        elif(e == 7):
                            break
                        else:
                            print("INVALID CHOICE")
                else:
                    print("BUYER NOT FOUND")
        elif(d == 2):
            print("NEW USER")
            new_user = {}
            name = input("ENTER NEW USER NAME: ")
            passwd = input("ENTER NEW USER PASSWORD: ")
            new_user['b_name'] = name
            new_user['passwd'] = passwd
            buyer.append(new_user)
            print("NEW USER ADDED SUCCESSFULLY")
        elif(d == 3):
            break
        else:
            print("INVALID CHOICE")


# driver code
print("WELCOME TO AMAZON")
while(True):
    print('''1.ADMIN\n2.MERCHANT\n3.BUYER\n4.EXIT''')
    n = int(input())
    if(n == 1):
        os.system('cls')
        print("WELCOME ADMIN")
        admins()
    elif(n == 2):
        os.system('cls')
        print("WELCOME MERCHANT")
        merchants()
    elif(n == 3):
        os.system('cls')
        print("WELCOME BUYER")
        buyers()
    elif(n == 4):
        exit()
    else:
        print("ENTER VALID INPUT")