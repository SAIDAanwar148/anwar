employees = [('vikram', 35,8.75),
             ('neha',30,12.50),
             ('charlie',50,15.50),
             ('rahul',20,7.00)]
for a in employees:
    name = a[0]
    wages = a[1]*a[2]
    print(f"{name} has to be paid ${wages} for this week")