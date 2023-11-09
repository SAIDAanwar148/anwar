list_num= list(input())
list=[]
for i in range (0,len(list_num)):
    min_num= min(list_num)
    list.append(min_num)
    list_num.remove(min_num)

print (list)


