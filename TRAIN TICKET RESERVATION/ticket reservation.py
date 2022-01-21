import os
admin = [{'ad_name': 'Admin1', 'passwd': 'admin1'}]
user=[{'name':'vijay','id':1,'passwd':'1234','wallet':1000},
        {'name':'user1','id':2,'passwd':'12','wallet':1000},
        {'name':'user2','id':3,'passwd':'123','wallet':1000}]
train=[{'train_name':'train1','stops':3,'seats':2,'seatarrangement':[[0 for i in range(3)] for j in range(2)],'stopname':[chr(65+i) for i in range(3)]}]
waiting_list=[]
booking_history=[]

def admins():
    while(True):
        print("\n1.ADD TRAIN\n2.REMOVE TRAIN\n3.VIEW SEAT\n4.EXIT")
        c=int(input("ENTER YOUR CHOICE ADMIN: "))
        if(c==1):
            os.system('cls')
            addtrain()
        elif(c==2):
            os.system('cls')
            removetrain()
        elif(c==3):
            os.system('cls')
            seatavailable()
        elif(c==4):
            break

def addtrain():
    d={}
    print("\t*** ADD TRAIN ***")
    print("\n")
    train_name=input("TRAIN NAME: ")
    stop=int(input("STOPS BTWN BOARDING AND DESTINATION: "))
    seat=int(input("NO OF SEATS: "))
    seat_array=[[0 for i in range(stop)] for j in range(seat)]
    stop_name=[]
    for i in range(stop):
        name=input("Enter stop name : ")
        stop_name.append(name)
            
    train.append({"train_name":train_name,'stops':stop,'seats':seat,'seatarrangement':seat_array,'stopname':stop_name})
         
def removetrain():
    print("\t*** REMOVE TRAIN ***")
    print("\n")
    name=input("TRAIN NAME: ")
    if(len(train)!=0):
        for i in train:
            if(i['train_name']==name):
                train.remove(i)
                print("TRAIN REMOVED")
                break
    else:
        print("NO TRAIN AVAILABLE")

def seatavailable():
    print("\t*** VIEW TRAINS ***")
    print("\n")
    if(len(train)!=0):
        for i in train:
            print("\t******")
            print("\nTRAIN NAME : ",i['train_name'])
            print("\n")
            print("SEAT AVAILABILITY IN",i['train_name'])
                    
            for j in i['seatarrangement']:
                print(j)
            print("\n")
            print("\nSTOPS IN",i['train_name'])
            k=0
            for x in i['stopname']:
                k+=1
                print("Stops",k,":",x)
    else:
        print("No train is available")

def users():
    os.system('cls')
    while(True):
        print("1.EXISTING USER\n2.NEW USER\n3.EXIT")
        n=int(input("ENTER YOUR CHOICE: "))
        if(n==1):
            name=input("ENTER YOUR USERNAME: ")
            passwd=input("ENTER YOUR PASSWORD: ")
            for i in user:
                if(i['name']==name and i['passwd']==passwd):
                    a=i

                    print("\nLOGGED IN SUCCESSFULLY\nWELCOME",a['name'])
                    while(True):
                        print("\n1.BOOK TICKET\n2.TICKET CANCELLATION\n3.VIEW BOOKING HISTORY\n4.SEAT ARRANGEMENTS\n5.EXIT")
                        m=int(input("ENTER YOUR CHOICE USER: "))
                        if(m==1):
                            os.system('cls')
                            bookticket(a)
                        elif(m==2):
                            cancelticket(a)
                        elif(m==3):
                            history(a)
                        elif(m==4):
                            userseat()
                        elif(m==5):
                            break
        elif(n==2):
            new={}
            while(True):
                print("1.CREATE\n2.EXIT")
                a=int(input("ENTER YOUR CHOICE: "))
                if(a==1):
                    for i in user:
                        name=input("ENTER NEW USER NAME: ")
                        if(name not in i['name']):
                            passwd=input("ENTER YOUR NEW USER PASSWD: ")
                            new['name']=name
                            new['id']=id+1
                            new['passwd']=passwd
                            user.append(new)
                            print(user)
                            print("USER ACCOUNT CREATED SUCCESSFULLY")
                            break
                    else:
                        print("USER NAME ALREADY TAKEN\nTRY DIFFERENT NAME")
                elif(a==2):
                    break
        elif(n==3):
            break

def bookticket(a):
    d={}
    wait={}
    flag=0
    print("\t*** BOOK TICKET **")
    val1=input("ENTER TRAIN NAME : ")
    k=0
    for w in user:
        if(w['name']==a['name']):
            f=w['id']
            #to display stops
    for y in train:
        if(y['train_name']==val1):
            for z in y['stopname']:
                k+=1
                print("Stops",k,":",z)
            #to alot seat
                #for p in range(1):
            sp=int(input("Enter boarding point : "))
            ep=int(input("Enter Destination : "))
            for i in range(y['seats']):
                if(sum(y['seatarrangement'][i][sp:ep])==0):
                    print("Seat alloted is",i)
                    flag=1
                    for j in range(sp-1,ep):
                        y['seatarrangement'][i][j]=f
                    break
            else:
                print("SEAT NOT AVAILABLE")
                flag=0
                wait['id']=f
                wait['passenger name']=a['name']
                wait['boarding point']=sp
                wait['destination']=ep
                waiting_list.append(wait)
                print("\nTICKET IS IN WAITING LIST")
                print("\n")
        if(flag==1):
            d['id']=f
            d['passenger name']=a['name']
            d['boarding point']=sp
            d['destination']=ep
            booking_history.append(d)
    print()

def cancelticket(a):
    os.system('cls')
    print("\t*** CANCEL YOUR BOOKING ***")
    history(a)
    s=int(input("BOARDING POINT : "))
    b=int(input("DESTINATION : "))
    r=int(input("ID : "))
    for i in booking_history:
        k=i['boarding point']
        v=i['destination']
        ab=i['id']
        ans1=abs(k-v)*r
        if(s==k and b==v and r==ab):
            for y in train:
                for i in range(y['seats']):
                    if(sum(y['seatarrangement'][i][k:v])==ans1):
                        for j in range(k-1,v):
                            y['seatarrangement'][i][j]=0
                        break
        for o in booking_history:
            if(o['passenger name']==a['name'] and o['boarding point']==s and o['destination']==b):
                booking_history.remove(o)
        print("BOOKING CANCELLED")
        for x in waiting_list:
            q=x['id']
            an=x['boarding point']
            c=x['destination']
            if(an==s and c==b):
                for y in train:
                     for i in range(y['seats']):
                        if(sum(y['seatarrangement'][i][an:c])==0):
                            for j in range(an-1,c):
                                y['seatarrangement'][i][j]=q
                            break
        
def history(a):
    print("\t*** BOOKING HISTORY ***")
    if(len(booking_history)!=0):
        for i in booking_history:
            if(i['passenger name']==a['name']):
                print("PASSENGER NAME : {}\nID : {},\nBOARDING POINT: {},\nDESTINATION: {} ".format(i['passenger name'],i['id'],i['boarding point'],i['destination']))
                print("\n")    
    else:
        print("NO BOOKING HISTORY FOUND")

def userseat():
    os.system('cls')
    print("\t*** VIEW TRAINS ***")
    print("\n")
    if(len(train)!=0):
        for i in train:
            print("*****")
            print("\nTRAIN NAME : ",i['train_name'])
            print("\n")
            print("SEAT AVAILABILITY IN",i['train_name'])
                    
        for j in i['seatarrangement']:
            print(j)
        print("\n")
        print("\nSTOPS IN",i['train_name'])
        k=0
        for x in i['stopname']:
            k+=1
            print("Stops",k,":",x)
    else:
        print("NO TRAIN AVAILABLE")
        

while(True):
    print("\n1.ADMIN\n2.USER\n3.EXIT")
    b=int(input("ENTER YOUR CHOICE: "))
    if(b==1):
        os.system('cls')
        name=input("ENTER ADMIN NAME: ")
        passwd=input("ENTER ADMIN PASSWORD: ")
        for i in admin:
            if(i['ad_name']==name and i['passwd']==passwd):
                print("\nWELCOME ADMIN")
                admins()
    elif(b==2):
        os.system('cls')
        users()
    elif(b==3):
        exit()