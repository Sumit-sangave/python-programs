n = int (input("enter a number:"))
a = n % 10
b = (int(n/10))%10
c = (int(n/100))%10
d = (int(n/1000))%10
nn = a**4 + b**4 + c**4 + d**4 
if(n == nn):

    print("Given number amstrong number.")
else:
    print("Given number is not a amstrong number.")