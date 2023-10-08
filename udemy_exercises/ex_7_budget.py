spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
 
low_spending = 0
normal_spending = 0
high_spending = 0

for month in spendings:
    if month < 1000.0:
        low_spending += 1
    elif month <= 2500.0:
        normal_spending += 1
    else:
        high_spending += 1 
print('Numbers of months with low spendings: ' + str(low_spending) + ', normal spendings: ' + str(normal_spending) + ', high spendings: ' + str(high_spending), end='.')