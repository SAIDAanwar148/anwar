import json

a= open("emploee.jason.txt", "r") 
b= a.read()
data = json.loads(b)
for employee in data['employees']:
    if employee [ "middleName"] == None:
           print(f"{ employee['id']}.{ employee['firstName']}{ employee['lastName']}@gmail.com") 
    else : 
        print(f"{employee['id']}.{ employee['firstName']}{ employee['middleName']}{ employee['lastName']}@gmail.com")
        
    details = json.dumps( employee, indent=(3))
    print(details)
