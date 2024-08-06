class bankcust:
    def __init__(self,sumit,sam123,samcom):
        self.custName=sumit
        self.password=sam123
        self.emailid=samcom

    def login(self):
        Name=input("Enter the name : ")
        Pwd=input("Enter the password : ")
        Email=input("Enter the email : ")
        if(Name==self.custName and Pwd==self.password and Email==self.emailid):
            print("Login Successfuly...!")
        else:
            print("Login Failed..!")
            
cust1=bankcust(" "," "," ")
cust1.login()  
