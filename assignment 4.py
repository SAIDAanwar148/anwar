a=open("assin.txt", 'r')
s=a.read()
firm=list(s.split())
wordcount=len(firm)
#a=open("assin.txt", 'w')
b=[]
for i in firm:
    c=i.lower()
    b.append(c)
dic={}  
for j in range(97,123):
    d=chr(j)
    count=0
    for i in s:
        if d==i:
            count+=1
    dic[d]=count
print (dic)
new_dic={}
for k,v in dic.items():
    value= v/wordcount
    new_dic[k]=value
print (new_dic)