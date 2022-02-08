import os
import datetime
import random
total_fine=20000
admin=[{'name':'admin1','pass':'1','email':'admin1@gmail.com'},{'name':'admin2','pass':'2','email':'admin2@gmail.com'}]
user=[{'name':'user1','pass':'1','email':'user1@gmail.com','wallet':30000,'two wheeler':0,'four wheeler':0},{'name':'user2','pass':'2','email':'user2@gmail.com','wallet':30000,'two wheeler':0,'four wheeler':0}]
vehicles=[{'brand name':'Duke','number plate':'ABC2000','type':'Two wheeler','rent':1000,'available count':1,'kms':0,'status':'available'},
            {'brand name':'Yamaha RX100','number plate':'ABC2001','type':'Two wheeler','rent':1000,'available count':1,'kms':0,'status':'available'},
            {'brand name':'RE','number plate':'ABC2002','type':'Two wheeler','rent':1000,'available count':1,'kms':0,'status':'available'},
            {'brand name':'Yamaha R15','number plate':'ABC2002','type':'Two wheeler','rent':1000,'available count':1,'kms':0,'status':'available'},
           {'brand name':'BMW','number plate':'ABC2500','type':'Four wheeler','rent':5000,'available count':1,'kms':0,'status':'available'},
           {'brand name':'Audi','number plate':'ABC2500','type':'Four wheeler','rent':5000,'available count':1,'kms':0,'status':'available'},
           {'brand name':'Benz','number plate':'ABC2500','type':'Four wheeler','rent':5000,'available count':1,'kms':0,'status':'available'}]

cart=[]

history=[]

print("\t----- ABC VEHICLE RENT-----")
print()
#generate random no
def randomnum():
    randomlist = []
    for i in range(1):
        n = random.randint(1000, 9000)
        randomlist.append(n)
    return randomlist[0]

#admin login
def admins():
    print("\t---- ADMIN LOGIN-----")
    print("1.Login\n2.Logout")
    b=int(input("Enter choice : "))
    if(b==1):
        os.system('cls')
        admin_email=input("\nEnter admin mail : ")
        admin_pass=input("\nEnter admin's password : ")
        for i in admin:
            if(i['email']==admin_email and i['pass']==admin_pass):
                print("\nWELCOME ",i['name'])
                admin_option()
                break
        else:
            print("\n----Admin not found----\n")

#admin options---->Add vehicle,modify vehicle,report,vehicle status
def admin_option():
    #os.system('cls')
    print("\t-----ADMIN OPTION-----")
    while(True):
        print("1.Add vehicle\n2.Modify vehicle\n3.Report\n4.Vehicle status\n5.Exit")
        print()
        a=int(input("Enter choice : "))
        if(a==1):#add vehicle
            os.system('cls')
            admin_add_vehicle()
        elif(a==2):
            os.system('cls')
            admin_modify_vehicle()
        elif(a==3):
            os.system('cls')
            admin_history()
        elif(a==4):
            os.system('cls')
            admin_update_status()
        elif(a==5):
            break

#admin option--->add vehicle
def admin_add_vehicle():
    os.system('cls')
    print("\t----- ADD VEHICLE -----")
    k=int(input("Enter no of vehicles to be added: "))
    for i in range(k):
        a=randomnum()
        v={}
        vehicle_name=input("Enter brand name : ")
        vehicle_type=input("Enter vehicle type : ")
        vehicle_rent=int(input("Enter vehicle rent  : "))
        count=int(input("Enter count : "))
        v['brand name']=vehicle_name
        v['number plate']="ABC"+str(a)
        v['type']=vehicle_type
        v['rent']=vehicle_rent
        v['available count']=count
        v['kms']=0
        v['status']='available'
        vehicles.append(v)
        print("Vehicle added successfully")

#admin options---->modify vehicle
def admin_modify_vehicle():
    os.system('cls')
    while(True):
        print("\t----- MODIFY VEHICLES -----")
        print("1.View available vehicles\n2.Remove vehicle\n3.Check vehicle count\n4.Update vehicle count\n5.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            os.system('cls')
            admin_view_vehicle()
        elif(a==2):
            os.system('cls')
            admin_remove_vehicle()
        elif(a==3):
            os.system('cls')
            admin_vehicle_count()
        elif(a==4):
            os.system('cls')
            admin_vehicle_count_update()
        elif(a==5):
            break

#admin options---->modify vehicles---->view vehicle
def admin_view_vehicle():
    os.system('cls')
    print("\t----- VIEW AVAILABLE VEHICLE -----")
    for i in vehicles:
        print("Brand Name :{}\t\tVechile Number :{}\nType :{}\t\tRent :{}\nAvailable count:{}\nKilometers used :{}\nStatus :{}".format(i['brand name'],i['number plate'],i['type'],i['rent'],i['available count'],i['kms'],i['status']))
        print("\n---------\n")

#admin options---->modify vehicles---->remove vehicle
def admin_remove_vehicle():
    os.system('cls')
    print("\t----- REMOVE VEHICLE-----")
    name=input("Enter vehicle name : ")
    for i in vehicles:
        if(i['brand name']==name):
            vehicles.remove(i)
            print("Vehicle removed successfully")
            break
    else:
        print("Vehicle not found")


#admin options---->modify vehicles---->check vehicle count
def admin_vehicle_count():
    os.system('cls')
    print("\t----- CHECK VEHICLE COUNT ----\n")
    for i in vehicles:
        print("Vehicle name : {}\nAvailable count :{}".format(i['brand name'],i['available count']))
        print()

#admin options---->modify vehicles---->update vehicle count
def admin_vehicle_count_update():
    os.system('cls')
    print("\t----- UPDATE VEHICLE COUNT -----")
    name=input("Enter vehicle name : ")
    for i in vehicles:
        if(i['brand name']==name):
            count=int(input("Enter Vehicle count : "))
            i['available count']+=count
            print("Vehicle count updated successfully")
            break
        else:
            print("Vehicle not found")
            break

#admin status
def admin_status():
    os.system('cls')
    print("\t----- ADMIN STATUS -----")
    while(True):
        print("1.See Status\n2.Update status\n3.Exit")
        k=int(input("Enter choice : "))
        if(k==1):
            admin_history()
        elif(k==2):
            admin_update_status()
        elif(k==3):
            break

#admin option --- see history
def admin_history():
    os.system('cls')
    print("\t----- VIEW HISTORY -----\n")
    if(len(history)!=0):
        for i in history:
            print("User name :{}\nBrand Name :{}\nVehicle number :{}\nType :{}\nRent : {}\nAvailable count :{}\nStatus :{}".format(i['name'],i['brand name'],i['vehicle number'],i['type'],i['rent'],i['available count'],i['status']))
            print()
    else:
        print("\nNo report found")

#admin option ---- update status
def admin_update_status():
    print("\t----- ADMIN UPDATE STATUS -----\n")
    print("1.Update status by Kilometers used\n2.Update status by condition\n")
    a=int(input("Enter choice : "))
    if(a==1):
        for i in vehicles:
            if(i['kms']>=3000):
                print("Vehicle name :{}\nKilometers :{}".format(i['brand name'],i['kms']))
                print("1.Unavailable\n2.Available")
                k=int(input("Enter choice : "))
                if(k==1):
                    i['status']='unavailable'
                else:
                    i['status']='available'
                break
        else:
            print("No vehicle is available")
    elif(a==2):
        for i in vehicles:
            if(i['status']=='low damage' or i['status']=='medium damage' or i['status']=='heavy damage'):
                print("Vehicle name :{}\nStatus :{}".format(i['brand name'],i['status']))
                print("1.Unavailable\n2.Available")
                k=int(input("Enter choice : "))
                if(k==1):
                    i['status']='unavailable'
                else:
                    i['status']='available'
                print()
        else:
            print("No vehicle is available")
    input("Press enter to continue")

#user login
def users():
    d={}
    print("\t---- USER LOGIN-----")
    print("1.Existing user\n2.New user")
    b=int(input("Enter choice : "))
    if(b==1):
        os.system('cls')
        user_mail=input("\nEnter user email : ")
        user_pass=input("\nEnter user's password : ")
        for i in user:
            if(i['email']==user_mail and i['pass']==user_pass):
                x=i
                print("\nWELCOME ",i['name'])
                user_option(x)
        else:
            print("\n----User not found----\n")
    elif(b==2):
        os.system('cls')
        print("\t----- CREATE YOUR ACCOUNT HERE -----")
        user_name=input("Enter user name : ")
        user_pass=input("Enter user password : ")
        user_mail=input("Enter user mail : ")
        user_wallet=int(input("Enter wallet amount : "))
        for i in user:
            if(i['email']==user_mail and i['pass']==user_pass):
                print("Email id already exist")
                break
            else:
                d['name']=user_name
                d['pass']=user_pass
                d['email']=user_mail
                d['wallet']=user_wallet
                d['two wheeler']=0
                d['four wheeler']=0
                user.append(d)
                print("User created succesfully\n")
                break

#user option
def user_option(x):
    os.system('cls')
    print("\t----- USER OPTIONS -----\n")
    while(True):
        print("1.Search vehicle\n2.Rent vehicle\n3.Cart\n4.Wallet\n5.View History\n6.Status\n7.Exit")
        k=int(input("Enter choice : "))
        if(k==1):
            os.system('cls')
            user_search_vehicle()
        elif(k==2):
            os.system('cls')
            user_rent_vehicle(x)
        elif(k==3):
            os.system('cls')
            user_cart(x)
        elif(k==4):
            os.system('cls')
            user_wallet(x)
        elif(k==5):
            os.system('cls')
            user_history(x)
        elif(k==6):
            os.system('cls')
            user_status(x)
        elif(k==7):
            break

#user option ---- search vehicle
def user_search_vehicle():
    os.system('cls')
    while(True):
        print("\t----- VIEW VEHICLE -----")
        print("1.Search by type\n2.Search by vehicle name\n3.Exit")
        a=int(input("Enter choice : "))
        if(a==1):
            os.system('cls')
            print("1.Two wheeler\n2.Four wheeler")
            n=int(input("Enter your choice : "))
            print()
            if(n==1):
                for i in vehicles:
                    if(i['type']=="Two wheeler"):
                        print("Brand Name :{}\t\tVechile Number :{}\nType :{}\t\tRent :{}\nAvailable count:{}\t\tKilometers used :{}\nStatus :{}".format(i['brand name'],i['number plate'],i['type'],i['rent'],i['available count'],i['kms'],i['status']))
                        print("-------------------------------")
                        print("1.Add to cart\n2.Next\n3.Exit\n")
                        b=int(input("Enter choice : "))
                        if(b==1):
                            cart.append(i)
                            print("Vehcile added to cart successfully")
                            print()
                            #print(cart)
                            input("Press enter to continue.........")
                            print()
                        elif(b==2):
                            continue
                        elif(b==3):
                            break

            elif(n==2):
                for i in vehicles:
                    if(i['type']=="Four wheeler"):
                        print("Brand Name :{}\t\tVechile Number :{}\nType :{}\t\tRent :{}\nAvailable count:{}\t\tKilometers used :{}\nStatus :{}".format(i['brand name'],i['number plate'],i['type'],i['rent'],i['available count'],i['kms'],i['status']))
                        print("--------------------------------")
                        print("1.Add to cart\n2.Next\n3.Exit\n")
                        b=int(input("Enter choice : "))
                        if(b==1):
                            cart.append(i)
                            print("Vehcile added to cart successfully")
                            print()
                            #print(cart)
                            input("Press enter to continue.........")
                            print()
                        elif(b==2):
                            continue
                        elif(b==3):
                            break
            elif(n==3):
                break
        elif(a==2):
            os.system('cls')
            print("\t----- SEARCH VEHICLE BY NAME -----\n")
            name=input("Enter vehicle name : ")
            for i in vehicles:
                if(i['brand name']==name):
                    print("Brand Name :{}\t\tVechile Number :{}\nType :{}\t\tRent :{}\nAvailable count:{}\nKilometers used :{}\nStatus :{}".format(i['brand name'],i['number plate'],i['type'],i['rent'],i['available count'],i['kms'],i['status']))
                    print("--------------------------------")
                    print("1.Add to cart\n2.Next\n3.Exit\n")
                    b=int(input("Enter choice : "))
                    if(b==1):
                        cart.append(i)
                        print("Vehcile added to cart successfully")
                            #print(cart)
                        input("Press enter to continue.........")
                        print()
                    elif(b==2):
                        continue
                    elif(b==3):
                        break

        elif(a==3):
            break

#user option -----Rent vehicle
def user_rent_vehicle(x):
    os.system('cls')
    h={}
    print("\t----- RENT VEHICLE -----\n")
    for i in cart:
        print("Brand Name :{}\t\tVechile Number :{}\nType :{}\t\tRent :{}\nAvailable count:{}\tKilometers used :{}\nStatus :{}".format(i['brand name'],i['number plate'],i['type'],i['rent'],i['available count'],i['kms'],i['status']))
        print()
    no=int(input("Enter no of vehicles to be rented : "))
    for i in range(no):
        if(len(cart)!=0):
            vehicle_name=input("Enter vehicle name to rent : ")
            for i in cart:
                types=i['type']
                if(i['brand name'])==vehicle_name:
                    print("1.Rent now\n2.Next\n3.Exit")
                    k=int(input("Enter choice : "))
                    if(k==1):
                        a=i['rent']
                        for j in user:
                            if(j['name']==x['name']):
                                if(j['wallet']>a and i['available count']>=1 and (j['two wheeler']<1 or j['four wheeler']<1) and i['status']=='available'):
                                    j['wallet']-=a
                                    i['available count']-=1
                                    if(types=="Two wheeler"):
                                        j['two wheeler']+=1
                                    elif(types=="Four wheeler"):
                                        j['four wheeler']+=1

                                    h['name']=x['name']
                                    h['brand name']=i['brand name']
                                    h['vehicle number']=i['number plate']
                                    h['type']=i['type']
                                    h['rent']=i['rent']
                                    h['available count']=i['available count']
                                    h['status']='rented'
                                    h['kms']=i['kms']
                                    h['date']=datetime.date.today()
                                    history.append(h)

                                    print("Vehicle rented and the rent amount is ",a)
                                    print()
                                    cart.remove(i)
                                    break
                                else:
                                    print("Vehicle not available")
                                    break
                    elif(k==2):
                        continue
                    elif(k==3):
                        break
        else:
            #print("\nNo product available in cart")
            break

#user option ---- Cart
def user_cart(x):
    while(True):
        print("1.View cart\n2.Add to cart\n3.Exit\n")
        a=int(input("Enter choice : "))
        if(a==1):
            user_view_cart(x)
        elif(a==2):
            user_search_vehicle()
        elif(a==3):
            break

#user option ---- view cart
def user_view_cart(x):
    os.system('cls')
    print("\t----- VIEW CART -----")
    if(len(cart)!=0):
        for i in cart:
            print("Brand Name :{}\t\tVechile Number :{}\nType :{}\t\tRent :{}\nAvailable count:{}\tKilometers used :{}\nStatus :{}".format(i['brand name'],i['number plate'],i['type'],i['rent'],i['available count'],i['kms'],i['status']))
            print()
    else:
        print("No vehicle available in cart")
        print()

#user option ---- transaction history
def user_history(x):
    os.system('cls')
    print("\t----- VIEW HISTORY -----\n")
    if(len(history)!=0):
        for i in history:
            if(x['name']==i['name']):
                print("User name :{}\nBrand Name :{}\nVehicle number :{}\nType :{}\nRent : {}\nAvailable count :{}\nStatus :{}".format(i['name'],i['brand name'],i['vehicle number'],i['type'],i['rent'],i['available count'],i['status']))
                print()
    else:
        print("No history found\n")

#user option ---- wallet
def user_wallet(x):
    os.system('cls')
    print("\t----- VIEW WALLET BALANCE -----\n")
    for i in user:
        if(x['name']==i['name']):
            print("Your wallet balance is ",i['wallet'])
            print()

#user option ----- status
def user_status(x):
    os.system('cls')
    print("\t----- USER STATUS -----")
    while(True):
        print("1.See Status\n2.Update status\n3.Exit")
        k=int(input("Enter choice : "))
        if(k==1):
            user_history(x)
        elif(k==2):
            user_update_status(x)
        elif(k==3):
            break

#user option ---- user update status
def user_update_status(x):
    os.system('cls')
    print("\t----- UPDATE THE STATUS OF RENTED VEHICLE -----")
    if(len(history)!=0):
        name=input("Enter vehicle name : ")
        kms=int(input("Enter kilometers : "))
        for i in history:
            if(x['name']==i['name'] and i['brand name']==name):
                print("1.Return Vehicle\n2.Loss\n")
                k=int(input("Enter choice : "))
                if(k==1):
                    for j in user:
                        if(j['name']==x['name']):
                            i['available count']+=1
                            print("1.Low damage\n2.Medium damage\n3.Heavy damage\n4.No damage")
                            d=int(input("Enter choice : "))
                            print()
                            if(d==1):
                                i['status']='low damage'
                                i['kms']+=kms
                                amount=total_fine*(20/100)
                                j['wallet']-=amount
                                print("Since you retured the vehicle with low damage,the fine amount collected was",amount)
                                print()
                            elif(d==2):
                                i['status']='medium damage'
                                i['kms']+=kms
                                amount=total_fine*(50/100)
                                j['wallet']-=amount
                                print("Since you retured the vehicle with medium damage,the fine amount collected was",amount)
                                print()
                            elif(d==3):
                                i['status']='heavy damage'
                                i['kms']+=kms
                                amount=total_fine*(75/100)
                                j['wallet']-=amount
                                print("Since you retured the vehicle with heavy damage,the fine amount collected was",amount)
                                print()
                            elif(d==4):
                                i['status']='returned with good condition'
                                i['kms']+=kms
                                if(kms>=500):
                                    amount=i['rent']*(15/100)
                                    j['wallet']-=amount
                                print("Vehicle returned")
                elif(k==2):
                    i['status']='lost'
                    print("Since you lost the vehicle,fine amount collected was",total_fine)
    else:
        print("\nYou have not rented any vehicle so far\n")     

#driver code
while(True):
    print("1.Admin\n2.User\n3.Exit\n")
    a=int(input("Enter choice : "))
    if(a==1):
        os.system('cls')
        admins()
    elif(a==2):
        os.system('cls')
        users()
    elif(a==3):
        exit()