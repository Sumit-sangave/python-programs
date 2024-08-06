n=int(input())
record=[]

for _ in range(0,n):
    name=input()
    marks=float(input())
    record.append([name,marks])

print(record)