a=int(input("Enter a number:"))
temp=0
while(a>0):
    temp+=a%10
    a=a//10

print(temp)