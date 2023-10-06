purchased_days = int(input('How many days ago have you purchased the item? '))
used = input('Have you used the item at all [y/n]? ')
broken = input('Has the item broken down on its own [y/n]? ')
 
if(broken == 'y' or (purchased_days <= 10 and used == 'n')):
  print('You can get a refund.')
else:
  print('You cannot get a refund.')