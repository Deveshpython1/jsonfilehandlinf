import json
import os

class Store:
    def __init__(self,data):
        self.data=data
        if os.path.exists("data1.json"):
            pass
        else:
            lis=[]
            with open("data1.json","w") as f:
                json.dump(lis,f)
    def store(self):
        with open("data1.json","r") as f:
            data1=json.load(f)
            l=[]
            l=data1
            l.append(self.data)
        with open("data1.json","w")as f:
            json.dump(l,f)

class Read:
    def __init__(self,accountnum):
        self.accountnum=accountnum
    def read(self):
        with open("data1.json","r") as f:
            data=json.load(f)
            l=[]
            for i in range(len(data)):               
                d=data[i].keys()
                key=list(d)
                l.append(key[0])
               
            def check():
             if str(self.accountnum) in l:
                return l.index(str(self.accountnum)),True
             else:
                return False
            if check():
                x=check()
                with open("data1.json","r") as f:
                    data=json.load(f)
                    print(data[x[0]][str(self.accountnum)]["Name"])
                    print(data[x[0]][str(self.accountnum)]["Age"])
                    print(data[x[0]][str(self.accountnum)]["Balance"])
                    return data,x[0]
            else:
                print("Account not found")

class Update(Read):
    def __init__(self, accountnum,credit=0,debit=0):
        Read.__init__(self,accountnum)
        val=Read.read(self)
        self.data=val[0]
        index=val[1]
        balance=self.data[index][str(accountnum)]["Balance"]
        balance=balance+credit-debit
        self.data[index][str(accountnum)]["Balance"]=balance
    def update(self):       
        with open("data1.json","w") as f:
            json.dump(self.data,f)
class Manage(Update,Read,Store):
    def __init__(self):
        pass 
    def createaccount(self):
        name=str(input("ENTER YOUR NAME"))
        age=int(input("ENTER AGE"))
        account=str(input("ENTER ANY 6 DIGIT NUMBER WHICH WILL BE YOUR ACCOUNT NUMBER"))
        import random
        l=[1000,2000,3000]
        balance=random.choice(l)
        dic={}
        dic[account]={"Name":name,"Age":age,"Balance":balance}
        Store.__init__(self,dic)
        Store.store(self)
        print("ACCOUNT CREATED SUCCESSFULLY")
    def Display(self):
        accountnum=str(input("ENTER ACCOUNT NUMBER"))
        Read.__init__(self,accountnum)
        Read.read(self)
    def Credit_and_debit(self):
        accountnum=str(input("ENTER ACCOUNT NUMBER"))
        c=int(input("ENTER AMOUNT TO CREDIT,IF DONT WANT ENTER 0"))
        d=int(input("ENTER AMOUNT TO DEBIT ,IF DONT WANT ENTER 0"))
        Update.__init__(self,accountnum,c,d)
        Update.update(self)
class Launch:
    def __init__(self):
     pass
    def Start(self):
     s="----------------ATM MENU-------------------\n1.CREATE ACCOUNT\n2.DISPLAY ACCOUNT DETAIL\n3.CREDIT AND DEBIT AMOUNT\n4.EXIT"
     print(s)
     val=int(input(""))
     match val:
       case 1:
         obj=Manage()
         obj.createaccount()
       case 2:
        obj=Manage()
        obj.Display()
       case 3:
        obj=Manage()
        obj.Credit_and_debit()
       case 4:
        pass
       case _:
          pass
obj=Launch()
obj.Start()




        
        



      
          
