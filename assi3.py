cardno=input('enter the card no ')
num=list(cardno)
check=int(num[-1])
num.pop(-1)
num.reverse()
size=len(num)
new=[]
for i in num:
    b=int(i)
    new.append(b)
for i in range(size):
    if i%2==0:
        new[i]=new[i]*2
for j in range (size):
    if new [j]>9:
        new[j]= new [j]-9
t= sum(new,check)
if t%10==0:
    print("card no is valid")
else:
      print("card no is not valid plz check the card")
