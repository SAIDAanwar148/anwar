import json

a= open("emploee.json", "r") 
b= a.read()
data = json.loads(b)
some={}
for employee in data['employees']:
    if employee [ "middleName"] == None:
           email=(f"{ employee['firstName']}{ employee['lastName']}@gmail.com") 
           name=(f"{ employee['firstName']}{ employee['lastName']}") 
    else : 
        email=(f"{ employee['firstName']}{ employee['middleName']}{ employee['lastName']}@gmail.com")
        name=(f"{ employee['firstName']}{ employee['middleName']}{ employee['lastName']}")
    some[email]={"id":employee["id"],  "fullname":name} 
work=json.dumps(some)
print(work)

#for i in data['employees']:
    #if employee ["middleName"]==None:
          #l=(f"{employee['id']}{ employee['firstName']}{ employee['lastName']}")
   # else:
   #       l=(f"{ employee['firstName']}{ employee['middleName']}{ employee['lastName']}")
   # some[l]=email
#print(some)
        
#details = json.dumps( employee, )
#some[details]=details
        
#print(some)
