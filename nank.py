class bankcust:
    def __init__(self,nm,pwd,mail):
        self.custName=nm
        self.password=pwd
        self.emailid=mail

    def login(self):
        Name=input("Enter the name : ")
        Pwd=input("Enter the password : ")
        Email=input("Enter the email : ")
        if(Name==self.custName and Pwd==self.password and Email==self.emailid):
            print("Login Successfuly...!")
        else:
            print("Login Failed..!")
            
cust1=bankcust("sumit","sumit123","s@gmail.com")
cust1.login()  



class bank:
    def __init__(self):
        self.amount=0
        
    def deposit(self,Amount):
        self.amount+=Amount
        print("Deposited Successfuly..!")
        
    def withdrawl(self,Amount):
        self.amount-=Amount
        print("Withdrawl Succeefuly..!")
     
    def display(self):
        print("Your bank balance is : ",self.amount)
cust1=bank()   

for _ in range(0,50):
    print("1.Deposit \n2.Withdrawl \n3.Display \n4.Exit")
    choise=(input("Enter the choise number : "))
    
    if(choise==1):
        Amount=int(input("Enter the amount to be deposited : "))
        cust1.deposit(Amount)
    elif(choise==2):
        Amount=int(input("Enter the amount to be withdrawl : "))
        cust1.withdrawl(Amount)
    elif(choise==3):
        Amount=cust1.display()
    elif(choise==4):
        exit()
    
    

            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        