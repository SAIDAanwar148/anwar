list_of_num=list(input())
length= len(list_of_num)
for i in range (0,length):
    for k in range (i+1,length):
        if list_of_num[i]>list_of_num[k]:
            list_of_num[i],list_of_num[k]=list_of_num[k],list_of_num[i]
print (list_of_num)