employees = [('vikram', 35,8.75),
             ('neha',30,12.50),
             ('charlie',50,15.50),
             ('rahul',20,7.00)] 
sumofallhourlywage = 0
for a in employees:
    hourlywage =a[2]
    sumofallhourlywage= sumofallhourlywage + hourlywage
avg =sumofallhourlywage/len(employees)
print (f'average hourly wage: ${avg}')
for b in employees:
    name = b[0]
    if b[2] <= avg:
        print (f'{name} earns less than the avg ')
    else:
        print (f'{name} earns more than the avg ')